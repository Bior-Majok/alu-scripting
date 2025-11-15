#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts of a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Python:API:top_ten:v1.0 (by /u/yourusername)"}

    try:
        # Do NOT follow redirects (allow_redirects=False)
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts[:10]:
            print(post["data"]["title"])

    except requests.RequestException:
        print(None)

