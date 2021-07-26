class Importer:

    keywords = [
        'python',
        'script',
        'scrape',
        'automation',
        'django',
        'flask',
        'bot',
        'vue',
        'nuxt',
        'backend',
        'back end',
        'front end',
        'frontend',
        'fullstack',
        'full stack',
        'ui/ux',
        'ui ux',
        'ui-ux',
        'logo',
    ]

    @classmethod
    def filter(cls, title, description):
        """Filtering items based on keywords that included in class"""
        title = title.strip().lower()
        description = description.strip().lower()
        if any(key in title for key in cls.keywords):
            return True
        if any(key in description for key in cls.keywords):
            return True
        return False
