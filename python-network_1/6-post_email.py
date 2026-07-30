#!/usr/bin/python3
"""Sends a POST request with an email parameter to a given URL,
using requests, and displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={"email": email})
    print(response.text)
