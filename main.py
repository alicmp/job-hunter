from utils.reddit import Reddit

if __name__ == "__main__":
    forhire = Reddit('forhire', 'Hiring')
    forhire.get_post_link()