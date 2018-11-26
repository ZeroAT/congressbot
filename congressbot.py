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

def check_if_bill_exists(id):
    reddit = bot_login()

    for post in reddit.subreddit('congresstests').search(id+":"):
        print("Searching subreddit for bill...")
        if post.title:
            return True
        else:
            return False




data = json.loads(response)

reddit = bot_login()


status = data["status"]
if get_status() == 'OK':
    for each in data['results'][0]['bills']:

        print(each.get("bill_id"))
        id = each.get("bill_id")
        title = each.get("title")
        url = each.get("congressdotgov_url")
        post_title = id + ": " + title

        if check_if_bill_exists(id) is True:
            print("This bill has already been posted.")
        else:
            print("Posting to Reddit...")
            reddit.subreddit('congresstests').submit(post_title, url=url)


