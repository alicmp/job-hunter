import os
from datetime import datetime

import praw


class Reddit:
    """Handle connecting to reddit and getting posts on specific subreddit"""

    def __init__(self, subreddits, flair, time_delta):
        self.subreddits = subreddits
        self.flair = flair.lower()
        self.time_delta = time_delta

    def get_post_link(self):
        """Getting posts link"""
        reddit = praw.Reddit(
            client_id=os.environ.get('reddit_personal_use_script'),
            client_secret=os.environ.get('reddit_secret'),
            user_agent=os.environ.get('reddit_app_name'),
            username=os.environ.get('reddit_username'),
            password=os.environ.get('reddit_password'),
        )

        for subreddit in self.subreddits:
            posts = reddit.subreddit(subreddit).new(limit=25)
            for post in posts:
                if not post.title:
                    continue
                post_created_time = datetime.utcfromtimestamp(post.created_utc)
                if self.flair in post.title.lower() and \
                    post_created_time >= self.time_delta:
                    yield {'title': post.title, 'description': post.selftext,
                           'url': post.url}
