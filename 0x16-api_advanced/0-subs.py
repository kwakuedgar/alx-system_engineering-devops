#!/usr/bin/python3
"""Request"""
import requests


def number_of_subscribers(subreddit):
    """Request subreddit"""
    url = 'https://api.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-agent': 'My Agent'}
    subred = requests.get(url, headers=header, allow_redirects=False)

    if subred.status_code != 200:
        return 0

    try:
        theme = subred.json()
    except:
        print("Not a valid JSON")
        return 0

    data = theme.get("data")
    if data:
        subscribers = data.get("subscribers")
        if subscribers:
            return subscribers

    return 0
