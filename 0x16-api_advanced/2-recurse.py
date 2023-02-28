#!/usr/bin/python3
"""
Script--> Query Reddit API recursively for all hot articles of a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], nxt="tmp"):
    """
        Return--> all hot articles given subreddit
        & return--> None if invalid subreddit given
    """
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    # URL update each recursive call with params "nxt"
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if nxt != "tmp":
        URL = URL + "?nxt={}".format(nxt)
    r = requests.get(URL, headers=headers, allow_redirects=False)

    # appending the top titles to hot_list[]
    res = r.json().get('data', {}).get('children', [])
    if not res:
        return hot_list
    for i in res:
        hot_list.append(i.get('data').get('title'))

    # get next parameter "nxt" else nothing else to recurse
    nxt = r.json().get('data').get('nxt')
    if not nxt:
        return hot_list
    return (recurse(subreddit, hot_list, nxt))
