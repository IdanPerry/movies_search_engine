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

from services.scrapers.content import ContentPage


class MoviesJoy(Thread):
    """
    This class manages MoviesJoy related content, which includes scraping the content
    and writing it to the related database using the views model.

    Inherits from Thread class.
    """

    MOVIES = 'https://moviesjoy.to/movie?page='
    TV_SHOWS = ''
    PAGES = 40

    def __init__(self, url: str):
        """
        Parameters
        ----------
        url : str
            The url to get the content from.
        """

        super().__init__()
        self._url = url
        self._content = []
        self._name = 'MoviesJoy'
        self.logger = logging.getLogger('scraping MoviesJoy')
        
    @property
    def name(self) -> str:
        return self._name
    
    def get_content(self) -> set:
        """
        Return
        ------
        List of movies or tv shows.
        """

        return set(self._content)

    def run(self):
        self.logger.debug('Importing MoviesJoy content...')
        urls = [f"{self._url}{page+1}" for page in range(self.PAGES)]
        self._content.extend(ContentPage.by_soup(urls).get_content('MoviesJoy', 'soup'))

        for item in self._content:
            item.source = self._name
