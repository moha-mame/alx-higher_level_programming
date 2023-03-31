#!/usr/bin/python3

"""
takes in a URL, sends a request to the URL & displays the body of the response
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    v = sys.argv

    try:
        with urllib.request.urlopen(v[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
