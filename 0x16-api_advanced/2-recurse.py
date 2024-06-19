#!/usr/bin/python3
"""
Module that recursively queries Reddit APU and returns list containning the
titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns list of all hot articles for a given subreddit
    """
    headers = {'User-Agent': 'My User Agent 1.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    resp = requests.get(url, headers=headers, allow_redirects=False,
                        timeout=120)
    if resp.status_code != 200:
        return None
    data = resp.json().get('data')
    after = data.get('after')
    children = data.get('children')
    for child in children:
        hot_list.append(child.get('data').get('title'))
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
