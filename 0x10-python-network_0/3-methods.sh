#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -sX OPTIONS -I $1 | grep -i 'allow' | awk -F ': ' '{print $2}'
