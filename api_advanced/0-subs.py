#!/usr/bin/python3
"""Module to query Reddit API for subreddit subscriber count."""
import requests


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of subscribers for a subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query
        
    Returns:
        int: Number of subscribers, or 0 if subreddit is invalid
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
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
    except Exception:
        return 0
