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

from services.pages.content import ContentPage


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

    MAX_PAGES = 4

    def __init__(self, content):
        """
        Parameters
        ----------
        content
        """

        super().__init__()
        self._content = content
        self.logger = logging.getLogger('scraping MoviesJoy')
        self._imported_content = []

    def get_content(self) -> list:
        """
        Return
        ------
        List of movies.
        """

        return self._imported_content

    def run(self):
        self.logger.debug('Importing MoviesJoy content...')

        for page in range(self.MAX_PAGES):
            url = f"{self._content['url']}{page+1}"
            self._imported_content.extend(ContentPage.by_soup(url).get_content('MoviesJoy', 'soup'))
            self._imported_content.sort()
