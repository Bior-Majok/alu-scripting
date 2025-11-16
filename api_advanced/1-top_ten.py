#!/usr/bin/python3
"""Module to query Reddit API for top 10 hot posts."""

import requests


def top_ten(subreddit):
    """
    Query the Reddit API and print titles of first 10 hot posts.

    Prints the titles of the first 10 hot posts listed for a given
    subreddit. If the subreddit is invalid or doesn't exist, prints None.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Python/requests:api_advanced:v1.0'}
    params = {'limit': 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

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
