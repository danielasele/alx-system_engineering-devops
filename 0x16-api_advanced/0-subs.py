#!/usr/bin/python3
"""
Script that queries the Reddit API to get the number of subscribers
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (compatible; Subreddit-Subscriber-Count/1.0)"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return (data['data'].get('subscribers', 0))
        else:
            return (0)
    except requests.RequestException:
        return (0)
