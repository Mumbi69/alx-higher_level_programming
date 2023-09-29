#!/usr/bin/python3
"""
takes your GitHub credentials (username and password) and
uses the GitHub API to display your id

"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <personal_access_token>")
        sys.exit(1)

    username = sys.argv[1]
    personal_access_token = sys.argv[2]

    # Define the GitHub API endpoint for user information
    api_url = 'https://api.github.com/user'

    # Set up the Basic Authentication
    auth = (username, personal_access_token)

    response = requests.get(api_url, auth=auth)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        user_data = response.json()
        print(user_data['id'])
    else:
        print(None)
