#!/usr/bin/python3
"""
0-subs.py

This module contains a function that queries the Reddit API and
returns the total number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return subscriber count for a subreddit or 0 if invalid"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ALUStudent/0.1"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get("data", {})
    return data.get("subscribers", 0)

