#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
[ -f "$2" ] && jq . < "$2" >/dev/null 2>&1 && curl -sX POST -H "Content-Type: application/json" -d "@$2" "$1"
