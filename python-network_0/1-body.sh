#!/bin/bash
# Sends a GET request to the given URL and displays the body of the
# response, but only if the status code is 200.
response=$(curl -s -w "\n%{http_code}" "$1")
status_code=$(echo "$response" | tail -n1)
body=$(echo "$response" | sed '$d')

if [ "$status_code" -eq 200 ]; then
    echo -n "$body"
fi
