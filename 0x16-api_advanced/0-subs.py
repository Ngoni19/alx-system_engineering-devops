#!/usr/bin/python3
"""
Query the Reddit API and returns the number of subscribers;
not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
        Return--> number of subscribers for a given subreddit;
        return 0 if invalid subreddit given
    """
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    r = requests.get(URL, headers=headers).json()
    subs = r.get('data', {}).get('subs')
    if not subs:
        return 0
    return subs
