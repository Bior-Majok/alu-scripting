#!/usr/bin/python3
"""Module to recursively query Reddit API for all hot posts."""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively query the Reddit API and return all hot article titles.

    Uses Reddit's pagination to retrieve all hot posts from a subreddit
    by recursively calling itself with the 'after' parameter until no
    more posts are available.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): List to accumulate post titles (default: None).
        after (str): Reddit's pagination token for the next page.

    Returns:
        list: A list of all hot post titles, or None if invalid subreddit.
    """
    if hot_list is None:
        hot_list = []

    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'linux:api_advanced:v1.0.0 (by /u/yourusername)'
    }
    params = {'limit': 100}
    
    if after:
        params['after'] = after

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )

        if response.status_code != 200:
            return None

        data = response.json()
        children = data.get('data', {}).get('children', [])
        after = data.get('data', {}).get('after', None)

        if len(children) == 0:
            if len(hot_list) == 0:
                return None
            return hot_list

        for child in children:
            post_data = child.get('data', {})
            title = post_data.get('title', None)
            if title:
                hot_list.append(title)

        if after is None:
            return hot_list

        return recurse(subreddit, hot_list, after)

    except (requests.RequestException, ValueError, KeyError):
        return None
