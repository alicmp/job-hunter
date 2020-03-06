class Importer:

    keywords = [
        'python',
        'instagram',
        'script',
        'django',
        'flask',
        'bot',
        'web'
    ]
    
    @classmethod
    def filter(cls, title, description):
        if any(key in title for key in cls.keywords):
            return True
        if any(key in description for key in cls.keywords):
            return True
        return False
