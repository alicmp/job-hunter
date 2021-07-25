class Importer:

    keywords = [
        'python',
        'instagram',
        'script',
        'django',
        'flask',
        'bot',
        'web'
        'vue',
        'nuxt',
        'backend',
        'back end',
        'front end',
        'frontend',
        'fullstack',
        'full stack'
        'ui'
        'ux',
    ]

    @classmethod
    def filter(cls, title, description):
        """Filtering items based on keywords that included in class"""
        title = title.lower()
        description = description.lower()
        if any(key in title for key in cls.keywords):
            return True
        if any(key in description for key in cls.keywords):
            return True
        return False
