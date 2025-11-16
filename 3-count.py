#!/usr/bin/python3
"""Module to recursively count keywords in Reddit hot posts."""

import requests


def count_words(subreddit, word_list, word_count=None, after=None):
    """
    Recursively query Reddit API and print sorted keyword counts.

    Parses titles of all hot articles in a subreddit and counts occurrences
    of given keywords. Results are printed in descending order by count,
    with alphabetical sorting for ties.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): List of keywords to count (case-insensitive).
        word_count (dict): Dictionary to track keyword counts.
        after (str): Reddit's pagination token for the next page.

    Returns:
        None: Prints results or nothing if invalid subreddit.
    """
    if word_count is None:
        word_count = {}
        for word in word_list:
            word_lower = word.lower()
            word_count[word_lower] = word_count.get(word_lower, 0)

    if subreddit is None or not isinstance(subreddit, str):
        return

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
            return

        data = response.json()
        children = data.get('data', {}).get('children', [])
        after_token = data.get('data', {}).get('after', None)

        if len(children) == 0:
            if after is None:
                print_results(word_count)
            return

        for child in children:
            post_data = child.get('data', {})
            title = post_data.get('title', '')
            if title:
                count_keywords(title, word_count)

        if after_token is None:
            print_results(word_count)
            return

        return count_words(subreddit, word_list, word_count, after_token)

    except (requests.RequestException, ValueError, KeyError):
        return


def count_keywords(title, word_count):
    """
    Count keyword occurrences in a title.

    Args:
        title (str): The post title to search.
        word_count (dict): Dictionary tracking keyword counts.
    """
    words = title.lower().split()
    
    for word in words:
        cleaned_word = ''.join(char for char in word if char.isalnum())
        if cleaned_word in word_count:
            word_count[cleaned_word] += 1


def print_results(word_count):
    """
    Print sorted keyword counts.

    Prints results in descending order by count, then alphabetically.
    Only prints keywords with at least one occurrence.

    Args:
        word_count (dict): Dictionary of keyword counts.
    """
    filtered = {k: v for k, v in word_count.items() if v > 0}
    
    if not filtered:
        return
    
    sorted_items = sorted(filtered.items(), key=lambda x: (-x[1], x[0]))
    
    for word, count in sorted_items:
        print("{}: {}".format(word, count))
