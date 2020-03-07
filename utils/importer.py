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
        """Filtering items based on keywords that included in class"""
        # TODO: instead of title and description get concatenation of both
        if any(key in title for key in cls.keywords):
            return True
        if any(key in description for key in cls.keywords):
            return True
        return False
