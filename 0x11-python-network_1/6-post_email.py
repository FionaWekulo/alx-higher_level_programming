#!/usr/bin/python3

"""A script that:
- takes in a URL and an email address,
- sends a POST request to the passed URL with the email as a parameter.
- and finally displays the body of the response.

"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    request = urllib.request.Request(url, value)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
