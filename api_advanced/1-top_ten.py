#!/usr/bin/python3
"""
Module to query Reddit API for top 10 hot posts
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit
    
    Returns:
        None: Prints titles or None if subreddit is invalid
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; RedditAPI/1.0)'}
    params = {'limit': 10}
    
    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
        
        # Check if the request was successful and not a redirect
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            
            if not posts:
                print(None)
                return
            
            for post in posts:
                title = post.get('data', {}).get('title')
                if title:
                    print(title)
        else:
            print(None)
    
    except Exception:
        print(None)
