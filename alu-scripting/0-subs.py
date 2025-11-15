#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a subreddit.
    If the subreddit is invalid, returns 0.
    """
    if subreddit is None or type(subreddit) is not str:
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "CustomUserAgent/1.0"
    }

    # Do NOT follow redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except ValueError:
        return 0

