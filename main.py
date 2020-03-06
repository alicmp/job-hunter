from utils.reddit import Reddit
from utils.importer import Importer

if __name__ == "__main__":
    forhire = Reddit(
        ['forhire', 'jobbit', 'jobopenings'],
        'Hiring'
    )
    reddit_results = forhire.get_post_link()
    for res in reddit_results:
        if Importer.filter(res['title'], res['description']):
            print(res)