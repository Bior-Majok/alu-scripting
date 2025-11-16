#!/usr/bin/python3
<<<<<<< HEAD
"""Return the umber of subscribers of a given subreddit"""

=======
"""Module to query Reddit API for subreddit subscriber count."""
>>>>>>> origin/main
import requests


def number_of_subscribers(subreddit):
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
        return 0
