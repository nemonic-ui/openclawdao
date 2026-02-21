from app.db import init_db
from app.x_api import fetch_user_profile


def run_agent() -> None:
    """Initialize dependencies and execute a sample X API workflow."""
    init_db()
    profile = fetch_user_profile("openai")
    print(f"Fetched profile: {profile}")
