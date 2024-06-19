#!/usr/bin/python3
"""
Module that interacts with Reddit API to get no. of subscribers of a subreddit
"""

import requests

headers = {'User-Agent': 'My User Agent 1.0'}


def number_of_subscribers(subreddit):
    """
    Returns number of subscribers of {subreddit}
    """
    resp = requests.get(
        f'https://www.reddit.com/r/{subreddit}/about.json',
        headers=headers,
        allow_redirects=False,
        timeout=120)
    if resp.status_code == 200:
        return (resp.json()['data']['subscribers'])
    else:
        return (0)
