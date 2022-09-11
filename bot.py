import praw

definition = "Testing is a procedure intended to ensure quality, performance or reliability"

reddit = praw.Reddit(client_id = "add your own here",
                     client_secret ="add your own here",
                     user_agent = "add what you want here",
                     username = "add your own here" ,
                     password = "add your own here")

subreddit = reddit.subreddit("testingground4bots")

for submission in subreddit.hot(limit = 10):
    for comment in submission.comments:
        if hasattr (comment , "body"):
                comment_lower = comment.body.lower()
                if ("test") in comment_lower:
                    comment.reply (definition)
