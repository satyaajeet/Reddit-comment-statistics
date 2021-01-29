#Inspired by u/Krukerfluk on Reddit

import praw
import time
reddit = praw.Reddit(
    client_id='your client id',
    client_secret='your client secret',
    username='jonathan_fortmann',
    password='your password',
    user_agent='your user agent')

while True:
    submission = reddit.submission(id='id from post')
    ratio = submission.upvote_ratio
    upvote = round((ratio * submission.score) / (2 * ratio - 1)) if ratio != 0.5 else round(submission.score / 2)
    try:
        top_comment1 = [comment.author for comment in submission.comments if (hasattr(comment, "body") and comment.distinguished == None)][0]
        if top_comment1 == None:
            top_comment1 = "[deleted]"
    except:
        top_comment1 = "Theres no place 1!"
    try:
        top_comment2 = [comment.author for comment in submission.comments if (hasattr(comment, "body") and comment.distinguished == None)][1]
        if top_comment2 == None:
            top_comment2 = "[deleted]"
    except:
        top_comment2 = "Theres no place 2!"
    try:
        top_comment3 = [comment.author for comment in submission.comments if (hasattr(comment, "body") and comment.distinguished == None)][2]
        if top_comment3 == None:
            top_comment3 = "[deleted]"
    except:
        top_comment3 = "Theres no place 3!"
    downvote = upvote - submission.score
    comments = str(submission.num_comments)


    new_body = f"""
Hello! I made a little Program
which gets statistics about this post!
It should be update every 20 seconds.

This post has {upvote} Upvotes!
-----
It has {downvote} Downvotes
-----
and {comments} comments!
-----

The 3 top comments are from:

1. {top_comment1}
2. {top_comment2}
3. {top_comment3}


This idea was inspired by u/Krukerfluk
Krukerfluk's post: https://www.reddit.com/r/Python/comments/hoolsm/this_post_has/
My code on Github: """

    submission.edit(new_body)
    time.sleep(20)
