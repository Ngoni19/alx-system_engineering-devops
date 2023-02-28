#!/usr/bin/python3
"""
Query Reddit API--> for titles of top ten posts given subreddit
"""
import requests


def top_ten(subreddit):
    """
        Retur--> top ten titles for a given subreddit
        Return--> None if invalid subreddit
    """
    
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    r = requests.get(URL, headers=headers).json()
    top_ten = r.get('data', {}).get('children', [])
    if not top_ten:
        print(None)
    for t in top_ten:
        print(t.get('data').get('title'))
