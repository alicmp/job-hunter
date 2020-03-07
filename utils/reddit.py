import os
import praw


class Reddit:
    """Handle connecting to reddit and getting posts on specific subreddit"""

    def __init__(self, subreddits, key_word):
        self.subreddits = subreddits
        self.key_word = key_word

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
            posts = reddit.subreddit(subreddit).search(self.key_word,
                                                       sort='new', limit=20)
            for post in posts:
                yield {'title': post.title, 'description': post.selftext,
                       'url': post.url}
