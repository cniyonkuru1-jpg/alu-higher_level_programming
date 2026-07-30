#!/bin/bash
# Sends an OPTIONS request to the given URL and displays all HTTP
# methods the server accepts.
curl -s -X OPTIONS -i "$1" | grep -i "Allow:" | cut -d' ' -f2- | tr -d '\r'
