import praw

definition = "Testing is a procedure intended to ensure quality, performance or reliability"

reddit = praw.Reddit(client_id = "I_U1nn1cRgYpUwDnOhllKg",
                     client_secret ="Vvp53u1K8S_lnwqsEg-_NcKC-qf0vg",
                     user_agent = "console:Portfolio:1.0",
                     username = "bot_for_portfolio" ,
                     password = "U6xHiXTL7k49QHG")

subreddit = reddit.subreddit("testingground4bots")

for submission in subreddit.hot(limit = 10):
    for comment in submission.comments:
        if hasattr (comment , "body"):
                comment_lower = comment.body.lower()
                if ("test") in comment_lower:
                    comment.reply (definition)