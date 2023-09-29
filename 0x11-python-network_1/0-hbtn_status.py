#!/usr/bin/python3
"""first script to fetch URL"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') \
            as response:
        html = response.read()
        utf8_html = html.decode('utf-8')

        print("Body response:")
        print(f"\t- type:", type(html))
        print(f"\t- content:", html)
        print(f"\t- utf8 content:", utf8_html)
