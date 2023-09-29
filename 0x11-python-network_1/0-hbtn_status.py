#!/usr/bin/python3
"""first script to fetch URL"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    utf8_html = html.decode('utf-8')

    print("Body response:")
    print("    - type:", type(html))
    print("    - content:", html)
    print("    - utf8 content:", utf8_html)
