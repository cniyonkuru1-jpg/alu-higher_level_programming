#!/bin/bash
# Sends a GET request to the given URL with a custom header
# X-HolbertonSchool-User-Id set to 98, and displays the body of the
# response.
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
