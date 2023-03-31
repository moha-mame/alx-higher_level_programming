#!/usr/bin/python3

"""
takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response
"""
if __name__ == "__main__":
    import urllib.request
    import sys

    v = sys.argv
    with urllib.request.urlopen(v[1]) as response:
        print(response.headers.get('X-Request-Id'))
