#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD
"""Return the umber of subscribers of a given subreddit"""

=======
"""Module to query Reddit API for subreddit subscriber count."""
>>>>>>> origin/main
=======
"""
0-subs.py

This module contains a function that queries the Reddit API and
returns the total number of subscribers for a given subreddit.
"""

>>>>>>> 9de0919ab5f3ba61cacfd94e82e3b3b218bd2398
import requests


def number_of_subscribers(subreddit):
<<<<<<< HEAD
<<<<<<< HEAD
    """function that fetches number_of_subscribers"""
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        return RESPONSE.json().get("data").get("subscribers")

=======
    """
    Query the Reddit API and return the number of subscribers for a subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query
        
    Returns:
        int: Number of subscribers, or 0 if subreddit is invalid
    """
   url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'linux:api_advanced:v1.0.0 (by /u/yourusername)'
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0
>>>>>>> origin/main
    except Exception:
=======
    """Return subscriber count for a subreddit or 0 if invalid"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ALUStudent/0.1"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
>>>>>>> 9de0919ab5f3ba61cacfd94e82e3b3b218bd2398
        return 0

    data = response.json().get("data", {})
    return data.get("subscribers", 0)

