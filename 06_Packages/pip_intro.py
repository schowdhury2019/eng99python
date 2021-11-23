# Pip Install Packages
# pip install requests

import ../05

import requests

requests_bbc = requests.get("https://www.bbc.co.uk")

print(requests_bbc, type(requests_bbc), repr(requests_bbc))
print(requests_bbc.headers)
print(requests_bbc.content)