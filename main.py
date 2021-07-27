import os
from datetime import datetime, timedelta

from utils.reddit import Reddit
from utils.importer import Importer
from utils.email import EmailHandler


def get_jobs():
    """Getting posts on different websites and filter their posts then return
    the filtered items.
    """
    forhire = Reddit(
        ['forhire', 'jobbit', 'jobopenings'],
        'Hiring',
        datetime.utcnow() - timedelta(hours=4) # an hour ago
    )
    reddit_results = forhire.get_post_link()
    for res in reddit_results:
        if Importer.filter(res['title'], res['description']):
            yield(res)



if __name__ == "__main__":
    """Printing results"""
    results = list(get_jobs())

    # Print jobs in console for development purpose
    for res in results:
        print(res['title'], res['url'])

    if results:
        sender_email = os.environ.get('sender_email')
        receiver_email = os.environ.get('receiver_email')
        password = os.environ.get('sender_email_password')

        time_period = datetime.now() - timedelta(hours=2)
        subject = f"Candid Jobs For {time_period} Until Now"
        email = EmailHandler(subject=subject, jobs=results,
                            sender_email=sender_email,
                            receiver_email=receiver_email, password=password)
        email.send_email()