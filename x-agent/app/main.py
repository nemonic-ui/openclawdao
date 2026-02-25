"""Entrypoint for the X-Agent service."""

from __future__ import annotations

import os
from datetime import datetime, timezone

from dotenv import load_dotenv


def main() -> None:
    """Start the X-Agent process."""
    load_dotenv()
    mode = os.getenv("X_AGENT_MODE", "standby")
    started_at = datetime.now(timezone.utc).isoformat()
    print(f"x-agent started in {mode} mode at {started_at}")


if __name__ == "__main__":
    main()
