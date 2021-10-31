"""
This module includes the class IMDb.

Classes
-------
IMDb
    Manages IMDb related content, which includes scraping the content
    and writing it to the related database using the views model.
"""

import logging
from threading import Thread

from services.pages.content import ContentPage
from content_data import views


class IMDb(Thread):
    """
    This class manages IMDb related content, which includes scraping the content
    and writing it to the related database using the views model.

    Inherits from Thread class.
    """

    CONTENT = {
        'movies': {'content_type': 'movie',
                   'url': 'https://www.imdb.com/search/title/?title_type=feature,tv_movie&count=250'},
        'tv-shows': {'content_type': 'tv-show',
                     'url': 'https://www.imdb.com/search/title/?title_type=tv_series&count=250'}
    }

    MAX_TITLES = 1000
    TITLES_PER_PAGE = 250

    def __init__(self, content):
        super().__init__()
        self._content = content
        self.logger = logging.getLogger('scraping IMDb')

    def run(self):
        self.logger.debug('Importing IMDb content...')
        imported_content = []

        # Iterating over all the pages
        for i in range(self.MAX_TITLES//self.TITLES_PER_PAGE):
            url = f"{self._content['url']}&start={i*self.TITLES_PER_PAGE + 1}&ref_=adv_nxt"
            imported_content.extend(ContentPage.by_soup(url).get_content('IMDb', 'soup'))
            imported_content.sort()

            # Insert movies to the database
            for item in imported_content:
                views.insert(item, self._content['content_type'])
