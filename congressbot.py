import praw

reddit = praw.Reddit(client_id='ztpKA8bDHobH6A',
                     client_secret='AhgsPPtXlUfjQFP-qoWQ5VB8fPk',
                     username='Zerotil',
                     password='passmod1',
                     user_agent='prawguide')

subreddit = reddit.subreddit('python')

hot_python = subreddit.hot(limit=5)

for submission in hot_python:
    if not submission.stickied:

        comments = submission.comments
        for comment in comments:
            print(20*'-')
            print(comment.body)

            if len(comment.replies) > 0:
                for reply in comment.replies:
                    print('REPLY: ', reply.body)