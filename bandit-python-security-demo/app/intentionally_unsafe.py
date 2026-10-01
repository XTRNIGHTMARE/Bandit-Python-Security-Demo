"""Intentionally unsafe code for Bandit static-analysis practice.

Do not run this file. Its unsafe patterns are included to produce findings.
"""

import hashlib
import subprocess


def weak_digest(text: str) -> str:
    """Return an MD5 digest; included only to demonstrate a finding."""
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def run_user_command(user_text: str) -> None:
    """Pass user-controlled text through a shell; included only for scanning."""
    subprocess.run("echo " + user_text, shell=True, check=False)
