import os
from typing import Any, Dict

import requests


BASE_URL = "https://api.x.com/2"


def fetch_user_profile(username: str) -> Dict[str, Any]:
    """Fetch a user profile from X API by username."""
    api_key = os.getenv("X_API_KEY", "")
    if not api_key:
        return {"error": "X_API_KEY is not configured"}

    headers = {"Authorization": f"Bearer {api_key}"}
    params = {"usernames": username}

    response = requests.get(f"{BASE_URL}/users/by", headers=headers, params=params, timeout=15)
    if response.status_code != 200:
        return {"error": response.text, "status_code": response.status_code}

    return response.json()
