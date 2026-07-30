#!/bin/bash
# Sends a POST request to the given URL with email and subject
# parameters, and displays the body of the response.
curl -s -X POST "$1" \
    -d "email=test@gmail.com" \
    -d "subject=I will always be here for PLD"
