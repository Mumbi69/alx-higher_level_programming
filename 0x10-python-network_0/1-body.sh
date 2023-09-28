#!/bin/bash
# Send a GET request using curl and display the body only if the response has a 200 status code
response_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
