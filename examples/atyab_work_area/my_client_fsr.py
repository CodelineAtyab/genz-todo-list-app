import requests


def fetch_profile(name="unknown", method="GET"):
    req_url = f"https://api.github.com/users/{name}"
    req_method = getattr(requests, method.lower())
    response = req_method(req_url)
    return response.status_code, response.json()
