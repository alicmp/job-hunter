import requests

class Importer:
    def __init__(self, url):
        self.url = url
    
    def get(self):
        res = requests.get(self)
        return res.text
