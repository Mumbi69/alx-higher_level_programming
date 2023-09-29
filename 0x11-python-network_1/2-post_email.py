#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)

"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    html = {'email': email}
    html = urllib.parse.urlencode(html).encode('utf-8')
    with urllib.request.urlopen(url, data=html) as response:
        response.html = response.read().decode('utf-8')
        print(response_data)
