#!/usr/bin/python3
""" calls the Reddit API and prints the titles of the first 10 hot posts """
import requests
def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "linux:1:v1.1 (by /u/heimer_r)"}
    params = {"limit": 10}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for unsuccessful responses
        data = response.json().get("data", {}).get("children", [])
        
        if not data:
            print("None")
        else:
            hot_titles = [post.get("data", {}).get("title") for post in data]
            print(*hot_titles, sep='\n')

    except requests.exceptions.RequestException as e:
        print("None")

# Example usage
top_ten('python')
