API_KEYS = {"testkey123": {"limit": 100}}

def verify_api_key(api_key: str) -> bool:
    return api_key in API_KEYS

def check_usage_limit(api_key: str) -> bool:
    from database.usage_tracker import get_usage
    return get_usage(api_key) < API_KEYS[api_key]["limit"]
