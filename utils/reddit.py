import os
import praw

from importer import Importer


class Reddit:

    def __init__(self, subreddit, key_word):
        self.subreddit = subreddit
        self.key_word = key_word
    

    def get_post_link(self):
        reddit = praw.Reddit(
            client_id=os.getenviron('reddit_personal_use_script'),
            client_secret=os.getenviron('reddit_secret'),
            user_agent=os.getenviron('reddit_app_name'),
            username=os.getenviron('reddit_username'),
            password=os.getenviron('reddit_password'),
        )
        subreddit = reddit.subreddit(self.subreddit)
        new_posts = subreddit.new(limit=20)
        
        for post in new_posts:
            print(post.title, post.id)