"""
This module includes the class MoviesJoy.

Classes
-------
MoviesJoy
    Manages MoviesJoy related content, which includes scraping the content
    and writing it to the related database using the views model.
"""

import logging
from threading import Thread

from content.pages.content import ContentPage
from content import views


class MoviesJoy(Thread):
    """
    This class manages MoviesJoy related content, which includes scraping the content
    and writing it to the related database using the views model.

    Inherits from Thread class.
    """

    CONTENT = {
        'movies': {'content_type': 'movie', 'url': 'https://moviesjoy.to/movie?page='},
        'tv-shows': {'content_type': 'tv-show', 'url': ''}
    }

    MAX_PAGES = 1

    def __init__(self, content):
        super().__init__()
        self._content = content
        self.logger = logging.getLogger('scraping MoviesJoy')

    def run(self):
        self.logger.debug('Importing MoviesJoy content...')
        imported_content = []

        for page in range(self.MAX_PAGES):
            url = f"{self._content['url']}{page+1}"
            imported_content.extend(ContentPage.by_soup(url).get_content('MoviesJoy', 'soup'))
            imported_content.sort()

            for item in imported_content:
                views.insert_content(item, 'MoviesJoy', self._content['content_type'])
