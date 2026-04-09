"""
GODMODE V8 — Groq Engine
Round-robin 4-key rate limiter with checkpoint persistence,
exponential backoff, and token budget tracking.
"""
from __future__ import annotations

import json
import logging
import os
import time
from pathlib import Path
from threading import Lock
from typing import Optional

import requests

logger = logging.getLogger(__name__)

CHECKPOINT_PATH = Path("data/checkpoint.json")
DAILY_REQUEST_LIMIT = 13_500        # Per key (leave 1.8% headroom from 13750)
DAILY_TOKEN_LIMIT = 950_000         # Per key (50k safety margin from 1M)
TOKENS_PER_REQUEST_SOFT_CAP = 800   # Output tokens per generation call
MAX_RETRIES = 4
BASE_BACKOFF = 2                    # Seconds; doubles each retry
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
DEFAULT_MODEL = "llama-3.3-70b-versatile"


class GroqKeyState:
    """Tracks usage state for a single Groq API key."""

    def __init__(self, key: str, index: int):
        self.key = key
        self.index = index
        self.requests_today = 0
        self.tokens_today = 0
        self.exhausted = False

    def has_capacity(self) -> bool:
        return (
            not self.exhausted
            and self.requests_today < DAILY_REQUEST_LIMIT
            and self.tokens_today < DAILY_TOKEN_LIMIT
        )

    def record_usage(self, tokens_used: int) -> None:
        self.requests_today += 1
        self.tokens_today += tokens_used
        if not self.has_capacity():
            self.exhausted = True
            logger.warning(f"Key {self.index + 1} exhausted for today.")

    def to_dict(self) -> dict:
        return {
            "index": self.index,
            "requests_today": self.requests_today,
            "tokens_today": self.tokens_today,
            "exhausted": self.exhausted,
        }

    def from_dict(self, data: dict) -> None:
        self.requests_today = data.get("requests_today", 0)
        self.tokens_today = data.get("tokens_today", 0)
        self.exhausted = data.get("exhausted", False)


class GroqEngine:
    """
    Production-grade Groq API engine with:
    - Round-robin 4-key rotation
    - Per-key daily token/request budgets
    - Exponential backoff on 429/5xx
    - Checkpoint save/restore for multi-day builds
    - Complete failure isolation (never corrupts calling code)
    """

    def __init__(self):
        raw_keys = [
            os.getenv("GROQ_API_KEY_1", ""),
            os.getenv("GROQ_API_KEY_2", ""),
            os.getenv("GROQ_API_KEY_3", ""),
            os.getenv("GROQ_API_KEY_4", ""),
        ]
        active_keys = [k.strip() for k in raw_keys if k.strip()]
        if not active_keys:
            raise EnvironmentError(
                "No Groq API keys found. Set GROQ_API_KEY_1 through GROQ_API_KEY_4 in .env"
            )

        self._keys: list[GroqKeyState] = [
            GroqKeyState(key, i) for i, key in enumerate(active_keys)
        ]
        self._current_index = 0
        self._lock = Lock()
        self._load_checkpoint()
        logger.info(f"GroqEngine initialised with {len(self._keys)} key(s).")

    # ------------------------------------------------------------------ #
    # Public API                                                           #
    # ------------------------------------------------------------------ #

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        max_tokens: int = TOKENS_PER_REQUEST_SOFT_CAP,
        temperature: float = 0.4,
    ) -> Optional[str]:
        """
        Send a generation request. Returns text or None on total failure.
        Never raises — callers are protected from crashes.
        """
        for attempt in range(MAX_RETRIES):
            key_state = self._pick_key()
            if key_state is None:
                logger.error("All Groq keys exhausted for today. Saving checkpoint.")
                self._save_checkpoint()
                return None

            try:
                response = self._call_api(key_state, system_prompt, user_prompt, max_tokens, temperature)
                self._save_checkpoint()
                return response
            except _RateLimitError as e:
                is_daily = "per day" in str(e).lower()
                limit_type = "Daily" if is_daily else "Per-Minute"
                
                # Use precise API reset header if available, otherwise fallback to backoff
                exact_wait = e.retry_after if e.retry_after > 0 else (BASE_BACKOFF ** (attempt + 1))
                wait = exact_wait if not is_daily else 0
                
                logger.warning(f"429 {limit_type} limit on key {key_state.index + 1}. Rotating. Backoff {wait:.1f}s.")
                if is_daily:
                    key_state.exhausted = True
                else:
                    time.sleep(wait)
            except _ServerError as e:
                wait = BASE_BACKOFF ** (attempt + 1)
                logger.warning(f"5xx on key {key_state.index + 1}. Backoff {wait}s. ({e})")
                time.sleep(wait)
            except Exception as e:
                logger.error(f"Unexpected Groq error: {e}", exc_info=True)
                return None

        logger.error("Max retries exceeded for Groq call. Skipping.")
        return None

    def total_requests_used(self) -> int:
        return sum(k.requests_today for k in self._keys)

    def total_tokens_used(self) -> int:
        return sum(k.tokens_today for k in self._keys)

    def all_keys_exhausted(self) -> bool:
        return all(not k.has_capacity() for k in self._keys)

    # ------------------------------------------------------------------ #
    # Internal helpers                                                     #
    # ------------------------------------------------------------------ #

    def _pick_key(self) -> Optional[GroqKeyState]:
        """Round-robin pick the next available key."""
        with self._lock:
            for _ in range(len(self._keys)):
                state = self._keys[self._current_index % len(self._keys)]
                self._current_index = (self._current_index + 1) % len(self._keys)
                if state.has_capacity():
                    return state
        return None

    def _call_api(
        self,
        key_state: GroqKeyState,
        system_prompt: str,
        user_prompt: str,
        max_tokens: int,
        temperature: float,
    ) -> str:
        headers = {
            "Authorization": f"Bearer {key_state.key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": DEFAULT_MODEL,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "max_tokens": max_tokens,
            "temperature": temperature,
            "stream": False,
        }
        resp = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=60)

        if resp.status_code == 429:
            # Extract exact reset time from headers directly (format like "4.5s")
            reset_str = resp.headers.get("x-ratelimit-reset-tokens", "") or resp.headers.get("x-ratelimit-reset-requests", "")
            try:
                wait_sec = float(reset_str.replace("s", "")) if reset_str else float(resp.headers.get("Retry-After", 2.0))
            except ValueError:
                wait_sec = 2.0
            raise _RateLimitError(resp.text, wait_sec)
        if resp.status_code >= 500:
            raise _ServerError(f"HTTP {resp.status_code}: {resp.text[:200]}")
        resp.raise_for_status()

        data = resp.json()
        content = data["choices"][0]["message"]["content"]
        tokens_used = data.get("usage", {}).get("total_tokens", max_tokens)
        key_state.record_usage(tokens_used)
        logger.debug(f"Key {key_state.index + 1}: {tokens_used} tokens used. "
                     f"Total today: {key_state.tokens_today:,}")
        return content

    def _save_checkpoint(self) -> None:
        try:
            data = {
                "saved_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "keys": [k.to_dict() for k in self._keys],
            }
            tmp = CHECKPOINT_PATH.with_suffix(".tmp")
            tmp.write_text(json.dumps(data, indent=2))
            tmp.replace(CHECKPOINT_PATH)
        except Exception as e:
            logger.warning(f"Failed to save checkpoint: {e}")

    def _load_checkpoint(self) -> None:
        if not CHECKPOINT_PATH.exists():
            return
        try:
            data = json.loads(CHECKPOINT_PATH.read_text())
            saved_date = data.get("saved_at", "")[:10]
            today = time.strftime("%Y-%m-%d", time.gmtime())
            if saved_date != today:
                logger.info("Checkpoint is from a previous day. Resetting counters.")
                CHECKPOINT_PATH.unlink(missing_ok=True)
                return
            for kd in data.get("keys", []):
                idx = kd.get("index", -1)
                if 0 <= idx < len(self._keys):
                    self._keys[idx].from_dict(kd)
            used = self.total_requests_used()
            logger.info(f"Checkpoint loaded. {used:,} requests already used today.")
        except Exception as e:
            logger.warning(f"Failed to load checkpoint: {e}. Starting fresh.")


class _RateLimitError(Exception):
    def __init__(self, message: str, retry_after: float = 0.0):
        super().__init__(message)
        self.retry_after = retry_after


class _ServerError(Exception):
    pass
