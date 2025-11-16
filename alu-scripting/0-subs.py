#!/usr/bin/python3
"""
Module that queries the Reddit API to return number of subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the total number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    if subreddit is None or type(subreddit) is not str:
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "CustomUserAgent/1.0"}

    try:
        res = requests.get(url, headers=headers, allow_redirects=False)

        # invalid subreddit → return 0
        if res.status_code != 200:
            return 0

        data = res.json()
        return data.get("data", {}).get("subscribers", 0)

    except Exception:
        return 0

