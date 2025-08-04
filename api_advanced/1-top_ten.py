#!/usr/bin/python3
"""" Top Ten Limit"""
import requests


def top_ten(subreddit):
    """"top ten"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10" \
        .format(subreddit)

    res = requests.get(url,
                       headers={
                           'User-Agent': 'Mozilla/5.0'})

    if res.status_code != 200:
        print(None)
    else:
        json_response = res.json()
        posts = json_response.get('data').get('children')
        [print(post.get('data').get('title')) for post in posts]#!/usr/bin/python3
"""Get the titles of the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):

    """Print titles of top 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None, end='')
        return
    posts = response.json().get('data', {}).get('children', [])
    for i in range(min(10, len(posts))):
        print(posts[i].get('data', {}).get('title', '').strip())
