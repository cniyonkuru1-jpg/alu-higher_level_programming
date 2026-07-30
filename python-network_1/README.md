# python-network_1

Python scripts that fetch and manipulate internet resources, first using
the standard library `urllib` package, then the third-party `requests`
package, covering GET/POST requests, headers, error handling, and JSON.

## Learning Objectives

- How to fetch internet resources with the Python package `urllib`
- How to decode a `urllib` body response
- How to use the Python package `requests`
- How to make HTTP GET and POST/PUT/etc. requests
- How to fetch JSON resources
- How to manipulate data from an external service

## Requirements

- All files interpreted with `python3` on Ubuntu 20.04 LTS
- Every file starts with `#!/usr/bin/python3`
- Code follows PEP 8 style
- Every file is executable
- Every module has a documentation string
- Code is not executed on import (`if __name__ == "__main__":`)

## Files

| File | Description |
| --- | --- |
| `0-hbtn_status.py` | Fetches the status endpoint using `urllib` |
| `1-hbtn_header.py` | Displays the `X-Request-Id` header, using `urllib` |
| `2-post_email.py` | POSTs an email parameter, using `urllib` |
| `3-error_code.py` | Handles `HTTPError` and prints the status code, using `urllib` |
| `4-hbtn_status.py` | Fetches the status endpoint using `requests` |
| `5-hbtn_header.py` | Displays the `X-Request-Id` header, using `requests` |
| `6-post_email.py` | POSTs an email parameter, using `requests` |
| `7-error_code.py` | Prints the status code for errors, using `requests` |
| `8-json_api.py` | Searches a user by letter and displays the JSON result |
| `10-my_github.py` | Displays a GitHub user's id via Basic Authentication |

## Author

Project completed as part of the ALU / Holberton higher-level programming track.
