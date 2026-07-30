#!/usr/bin/python3
"""Sends a request to a given URL and displays the body of the
response, handling HTTPError exceptions by printing the status
code, using urllib.
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
