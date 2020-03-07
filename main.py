from utils.reddit import Reddit
from utils.importer import Importer


def main():
    """Getting posts on different websites and filter their posts then return
    the filtered items.
    """
    forhire = Reddit(
        ['forhire', 'jobbit', 'jobopenings'],
        'Hiring'
    )
    reddit_results = forhire.get_post_link()
    for res in reddit_results:
        if Importer.filter(res['title'], res['description']):
            yield(res)



if __name__ == "__main__":
    """Printing results"""
    results = main()
    for res in results:
        print(res['title'])