# Job Hunter
I wrote this bot to find job postings from reddit and craigslist (in the future)
based on my preferences. And email them to me. The bots workflow is simple, It 
first connects to reddit,and catches submissions from my chosen subreddits. 
After that it filters the submissions based on my preferences and finally email 
them to my email!

## Requirements
- Python 3.8
- Pipenv

## Setup
create the `.env` file and put necessary information inside it. You can check 
`.env.sample` to find out which information you need.
Navigate to the root of the project and activate virtual environment.
``` sh
$ pipenv shell
```
Install dependencies.
``` sh
$ pipenv sync
```
Edit keyword on `utils/importer.py` based on your own preferences.
And finally run the code.
``` sh
$ python main.py
```
You can use cronjob to run the code periodically.

## Future development
- [] Write Craigslist importer as well.
- [] Create webapp and let other users enter their email and their tech and send 
related job posts to their email.
- [] Use spaCy for filtering relatable job posts.