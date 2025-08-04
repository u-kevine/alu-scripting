#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'python:api_advanced:v1.0 (by /u/Comfortable_Net_1144)'  
    }
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get('data', {}).get('children', [])

        for post in posts:
            print(post['data'].get('title'))

    except Exception:
        print(None)
