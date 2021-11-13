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

from services.scrapers.content import ContentPage


class IMDb(Thread):
    """
    This class manages IMDb related content, which includes scraping the content
    and writing it to the related database using  content_data.views module.

    Inherits from Thread class.
    """

    MOVIES = 'https://www.imdb.com/search/title/?title_type=feature,tv_movie&count=250'
    TV_SHOWS = 'https://www.imdb.com/search/title/?title_type=tv_series&count=250'
    MAX_TITLES = 5000
    TITLES_PER_PAGE = 250
    PAGES = MAX_TITLES // TITLES_PER_PAGE

    def __init__(self, url):
        super().__init__()
        self._url = url
        self._content = []
        self.logger = logging.getLogger('scraping IMDb')

    def get_content(self) -> set:
        """
        Return
        ------
        List of movies or tv shows.
        """

        return set(self._content)

    def run(self):
        self.logger.debug('Importing IMDb content...')
        urls = [f"{self._url}&start={i*self.TITLES_PER_PAGE + 1}&ref_=adv_nxt" for i in range(self.PAGES)]
        self._content = ContentPage.by_soup(urls).get_content('IMDb', 'soup')
