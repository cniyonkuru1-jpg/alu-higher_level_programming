#!/usr/bin/python3
"""Displays the value of the X-Request-Id header found in the
response of a request sent to a given URL, using requests.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
