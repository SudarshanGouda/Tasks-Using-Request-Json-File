"""
pip - pip installs packages - package installer

PyPi - Python Package index - list of external packages written in Python

WRITE a function that will open website provided as argument

"""

import requests

responce= requests.get('http://github.com/SudarshanGouda')

print(responce)
