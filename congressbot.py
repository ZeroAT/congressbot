import praw
import requests
import json

def bot_login():
    print("Using API Info to Login...")
    reddit = praw.Reddit(client_id='ztpKA8bDHobH6A',
                         client_secret='AhgsPPtXlUfjQFP-qoWQ5VB8fPk',
                         username='Zerotil',
                         password='',
                         user_agent='prawguide')
    return reddit

def get_status(data):
    status = data["status"]
    print("Status: " + status)

    return status

def check_if_bill_exists(id, reddit):
    for post in reddit.subreddit('congresstests').search(id+":"):
        print("Searching subreddit for bill...")
        if post.title:
            return True
        else:
            return False

def get_recent_bills(reddit):
    response = requests.get("https://api.propublica.org/congress/v1/115/house/bills/introduced.json", headers={'X-API-Key': 'x2lvYYuxgWmzInlfwUOAqS2LBm7uSpwz8y2aUx7b'}).content

    data = json.loads(response)


    if get_status(data) == 'OK':
        for each in data['results'][0]['bills']:

            print(each.get("bill_id"))
            id = each.get("bill_id")
            title = each.get("title")
            url = each.get("congressdotgov_url")
            post_title = id + ": " + title

            if check_if_bill_exists(id, reddit) is True:
                print("This bill has already been posted.")
            else:
                print("Posting to Reddit...")
                reddit.subreddit('congresstests').submit(post_title, url=url)





reddit = bot_login()
get_recent_bills(reddit)

