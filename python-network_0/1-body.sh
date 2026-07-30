#!/bin/bash
# Sends a GET request (following redirects) and displays the body only if final status is 200
curl -sL -w "%{http_code}" -o /tmp/body_$$ "$1" | grep -q "^200$" && cat /tmp/body_$$; rm -f /tmp/body_$$
