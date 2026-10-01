"""Safer alternatives for comparison with intentionally_unsafe.py."""

import hashlib


def sha256_digest(text: str) -> str:
    """Return a SHA-256 digest for a non-password integrity example."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def format_message(message: str) -> str:
    """Format text using Python without launching a shell process."""
    return f"Message: {message}"
