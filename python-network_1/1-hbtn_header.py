#!/usr/bin/python3
"""Displays the value of the X-Request-Id header found in the
response of a request sent to a given URL, using urllib.
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.getheader("X-Request-Id"))
