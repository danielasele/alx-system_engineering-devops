#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom_user_agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return (data['data'].get('subscribers', 0))
    return (0)
