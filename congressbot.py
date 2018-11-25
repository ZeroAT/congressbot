import praw
import requests
import json

def bot_login():
    print("Using API Info to Login...")
    reddit = praw.Reddit(client_id='ztpKA8bDHobH6A',
                         client_secret='AhgsPPtXlUfjQFP-qoWQ5VB8fPk',
                         username='Zerotil',
                         password='passmod1',
                         user_agent='prawguide')
    return reddit

def get_status():
    status = data["status"]
    print("Status: OK")

    return status


response = requests.get("https://api.propublica.org/congress/v1/115/house/bills/introduced.json", headers={'X-API-Key': 'x2lvYYuxgWmzInlfwUOAqS2LBm7uSpwz8y2aUx7b'}).content


data = json.loads(response)

status = data["status"]
if get_status() == 'OK':
    for each in data['results'][0]['bills']:
        print(each.get("bill_id"))

