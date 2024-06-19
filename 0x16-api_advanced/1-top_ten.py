#!/usr/bin/python3
"""
Module that queries Reddit API to print first 10 hot posts for a given sub
"""

import requests


def top_ten(subreddit):
    """
    Returns top 10 posts for {subreddit}
    """
    resp = requests.get(
        f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10',
        allow_redirects=False,
        headers=headers,
        timeout=120
    )
    if resp.status_code == 200:
        for post in resp.json()['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
