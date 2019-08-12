from utils.reddit import Reddit

if __name__ == "__main__":
    forhire = Reddit(
        ['forhire', 'jobbit', 'jobopenings'],
        'Hiring'
    )
    forhire.get_post_link()