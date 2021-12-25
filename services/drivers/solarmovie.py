"""
This module includes the class Solarmovie.

Classes
-------
Solarmovie
    Manages Solarmovie related content, which includes scraping the content
    and writing it to the related database using the views model.
"""

import logging
from threading import Thread

from services.scrapers.content import ContentPage


class Solarmovie(Thread):
    """
    This class manages Solarmovie related content, which includes scraping the content
    and writing it to the related database using the views model.

    Inherits from Thread class.
    """

    MOVIES = 'https://www2.solarmovie.to/movie/filter/movies/page-'
    TV_SHOWS = ''
    MAX_PAGES = 550
    PAGES = 100

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
        self._name = 'Solarmovie'
        self.logger = logging.getLogger('scraping Solarmovie')

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
        self.logger.debug('Importing Solarmovie content...')
        urls = [f"{self._url}{page+1}.html" for page in range(self.PAGES)]
        self._content.extend(ContentPage.by_soup(urls).get_content('Solar', 'soup'))

        for item in self._content:
            item.source = self._name
