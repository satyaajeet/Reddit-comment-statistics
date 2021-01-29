#Inspired by u/Krukerfluk on Reddit
#Feel free to edit/use my code!
import praw
import time
import datetime

def print_first_word(mystring):
    return mystring.split().pop(0)
    

post_id = "*****"
reddit = praw.Reddit(
    client_id='*****',
    client_secret='*****',
    username='*****',
    password='*****',
    user_agent='*****')
try:
    with open("total_updates.txt", "x") as f:
        pass
    with open("total_updates.txt", "w") as f:
        f.write("0")
except:
    pass
while True:
    with open("total_updates.txt", "r") as f:
        update_number = f.read()
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    submission = reddit.submission(id=post_id)
    latest_post = reddit.submission(id=post_id)
    latest_post.comment_sort = 'new'
    ratio = submission.upvote_ratio
    upvote = round((ratio * submission.score) / (2 * ratio - 1)) if ratio != 0.5 else round(submission.score / 2)

    last_comment = [comment.author for comment in latest_post.comments if(hasattr(comment, "body") and comment.distinguished == None)][0]
    print(last_comment)

    try:
        top_comment1 = [comment.author for comment in submission.comments if (hasattr(comment, "body") and comment.distinguished == None)][0]
        top_word1 = [comment.body for comment in submission.comments if(hasattr(comment, "body") and comment.distinguished == None)][0]
        if top_comment1 == None:
            top_comment1 = "[deleted]"
    except Exception as e:
        print(e)
        top_comment1 = "Theres no place 1!"

    try:
        top_comment2 = [comment.author for comment in submission.comments if (hasattr(comment, "body") and comment.distinguished == None)][1]
        top_word2 = [comment.body for comment in submission.comments if (hasattr(comment, "body") and comment.distinguished == None)][1]
        if top_comment2 == None:
            top_comment2 = "[deleted]"
    except:
        top_comment2 = "Theres no place 2!"
    try:
        top_comment3 = [comment.author for comment in submission.comments if (hasattr(comment, "body") and comment.distinguished == None)][2]
        top_word3 = [comment.body for comment in submission.comments if (hasattr(comment, "body") and comment.distinguished == None)][2]
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

    |_First word: {print_first_word(top_word1)}

2. {top_comment2}

    |_First word: {print_first_word(top_word2)}

3. {top_comment3}

    |_First word: {print_first_word(top_word3)}


latest comment by: {last_comment}

Last update: {current_time} CET

total updates: {str(int(update_number) + int(1))}


This idea was inspired by u/Krukerfluk
Krukerfluk's post: https://www.reddit.com/r/Python/comments/hoolsm/this_post_has/

My code on Github: https://github.com/Jonathan357611/Reddit-comment-statistics

This program is hosted on a Raspberry pi zero!"""
    submission.edit(new_body)

    with open("total_updates.txt", "w") as f:
        f.write(str(int(update_number) + int(1)))
    time.sleep(20)
