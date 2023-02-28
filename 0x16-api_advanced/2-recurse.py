#!/usr/bin/python3
"""
Script --> Query Reddit API recursively for
all hot articles of a given subreddit;If no res are found;
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

    # URL update--> each recursive call with param "aft"
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if aft != "tmp":
        URL = URL + "?aft={}".format(aft)
    r = requests.get(URL, headers=headers, allow_redirects=False)

    # append top titles to hot_list[]
    res = r.json().get('data', {}).get('children', [])
    if not res:
        return hot_list
    for i in res:
        hot_list.append(i.get('data').get('title'))

    # get next params "aft" else nothing to recurse
    aft = r.json().get('data').get('aft')
    if not aft:
        return hot_list
    return (recurse(subreddit, hot_list, aft))
