# python-network_0

Bash scripts using curl to interact with a web server: checking response body size, following redirects, sending DELETE/POST requests, custom headers, and discovering allowed HTTP methods.

## Tasks

0. `0-body_size.sh` - Displays the size (in bytes) of the response body for a given URL.
1. `1-body.sh` - Sends a GET request (following redirects) and displays the body only if the final status is 200.
2. `2-delete.sh` - Sends a DELETE request and displays the response body.
3. `3-methods.sh` - Displays all HTTP methods the server accepts for a given URL.
4. `4-header.sh` - Sends a GET request with a custom `X-HolbertonSchool-User-Id: 98` header and displays the body.
5. `5-post_params.sh` - Sends a POST request with `email` and `subject` parameters and displays the body.
