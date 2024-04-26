#!/usr/bin/python3
"""
Display the X-Request-Id variable value
in the header of the response
"""
import urllib.request
from sys import argv


def main(argv):
    """
    Process that takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable
    in the header of the response
    """
    url = argv
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        print(headers['X-Request-Id'])


if __name__ == "__main__":
    main(argv[1])
