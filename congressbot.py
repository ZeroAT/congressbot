import praw
import requests
import json

response = requests.get("https://api.propublica.org/congress/v1/115/house/bills/introduced.json", headers={'X-API-Key': 'x2lvYYuxgWmzInlfwUOAqS2LBm7uSpwz8y2aUx7b'})

print(response.status_code)

if response.status_code == requests.codes.ok:
    response_native = json.loads(response.text)
    print(response_native)
