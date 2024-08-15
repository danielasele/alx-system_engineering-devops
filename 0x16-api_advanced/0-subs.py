#!/usr/bin/python3
"""
Script to query the Reddit API and retrieve the number of subscribers
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a given subreddit."""
    if not subreddit or type(subreddit) is not str:
        return (0)
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Subreddit-Subscriber-Count/1.0)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            return (data.get('subscribers', 0))
        return (0)
    except requests.RequestException:
        return (0)
