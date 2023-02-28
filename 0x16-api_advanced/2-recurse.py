#!/usr/bin/python3
"""
Script --> Query Reddit API recursively for
all hot articles of a given subreddit;If no results are found;
for the given subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], aft="tmp"):
    """
        Return--> all hot articles for a given subreddit
        &return; None if invalid subreddit given
    """
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    # update url each recursive call with param "aft"
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if aft != "tmp":
        url = url + "?aft={}".format(aft)
    r = requests.get(url, headers=headers, allow_redirects=False)

    # append top titles to hot_list[]
    results = r.json().get('data', {}).get('children', [])
    if not results:
        return hot_list
    for e in results:
        hot_list.append(e.get('data').get('title'))

    # get next param "aft" else nothing else to recurse
    aft = r.json().get('data').get('aft')
    if not aft:
        return hot_list
    return (recurse(subreddit, hot_list, aft))
