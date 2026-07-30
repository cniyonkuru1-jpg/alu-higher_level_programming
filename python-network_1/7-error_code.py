#!/usr/bin/python3
"""Sends a request to a given URL and displays the body of the
response, or an error message if the status code is 400 or above,
using requests.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
