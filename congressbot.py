import praw
import requests
import json

response = requests.get("https://api.propublica.org/congress/v1/115/house/bills/introduced.json", headers={'X-API-Key': 'x2lvYYuxgWmzInlfwUOAqS2LBm7uSpwz8y2aUx7b'}).content


data = json.loads(response)

status = data["status"]

if status == 'OK':
    for each in data['results'][0]['bills']:
        print(each.get("bill_id"))

test = data['results'][0]['bills'][0]['bill_id']

