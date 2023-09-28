#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -sX OPTIONS -I $1 | grep -i "Allow" | awk '{print $2}'
