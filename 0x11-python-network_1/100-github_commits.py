#!/usr/bin/python3
"""
takes 2 arguments in order to solve this challenge.

"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository> <owner>")
        sys.exit(1)

    repository = sys.argv[1]
    owner = sys.argv[2]

    # Define the GitHub API endpoint for retrieving commits
    api_url = f'https://api.github.com/repos/{owner}/{repository}/commits'

    # Send a GET request to the GitHub API endpoint
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        commits = response.json()

        # Print the 10 most recent commits
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")

    else:
        print("Error:", response.status_code)
