import os
from datetime import datetime, timedelta

from utils.reddit import Reddit
from utils.importer import Importer
from utils.email import EmailHandler
from utils.logging_helper import logging


HOURS_OFFSET = 4


def get_jobs():
    """Getting posts on different websites and filter their posts then return
    the filtered items.
    """
    forhire = Reddit(
        ['forhire', 'jobbit', 'jobopenings'],
        'Hiring',
        datetime.utcnow() - timedelta(hours=HOURS_OFFSET)
    )
    final_results = []
    reddit_results = list(forhire.get_post_link())

    logging.info(f'got {len(reddit_results)} results from reddit since {HOURS_OFFSET} hours ago')

    for res in reddit_results:
        if Importer.filter(res['title'], res['description']):
            final_results.append(res)

    logging.info(f'got {len(final_results)} results after filtering them')

    return final_results


if __name__ == "__main__":
    """getting results and emailing them"""
    results = get_jobs()

    if results:
        sender_email = os.environ.get('sender_email')
        receiver_email = os.environ.get('receiver_email')
        password = os.environ.get('sender_email_password')

        time_period = datetime.now() - timedelta(hours=HOURS_OFFSET)
        subject = f"Candid Jobs For {time_period.strftime('%d-%b-%y %H:%M:%S')} Until Now"
        email = EmailHandler(subject=subject, jobs=results,
                            sender_email=sender_email,
                            receiver_email=receiver_email, password=password)
        email.send_email()
        logging.info('email sent')