import os
import praw


class Reddit:

    def __init__(self, subreddit, key_word):
        self.subreddit = subreddit
        self.key_word = key_word
    

    def get_post_link(self):
        reddit = praw.Reddit(
            client_id=os.environ.get('reddit_personal_use_script'),
            client_secret=os.environ.get('reddit_secret'),
            user_agent=os.environ.get('reddit_app_name'),
            username=os.environ.get('reddit_username'),
            password=os.environ.get('reddit_password'),
        )
        subreddit = reddit.subreddit(self.subreddit)
        new_posts = subreddit.new(limit=100)

        for post in new_posts:
            if self.key_word in post.title:
                print(post.title, post.id, post.url)