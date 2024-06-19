#!/usr/bin/python3
"""
Module that recursively queries Reddit API, parses the title of all hot
        articles, and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, hot_list=[], after=None, word_count={}):
    """
    Returns a sorted count of given keywords
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
        return count_words(subreddit, word_list, hot_list, after, word_count)
    for title in hot_list:
        for word in word_list:
            if word.lower() in title.lower():
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    for word in sorted(word_count, key=word_count.get, reverse=True):
        if word_count[word] != 0:
            print(f'{word}: {word_count[word]}')
