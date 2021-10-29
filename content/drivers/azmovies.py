"""
This module includes the class AZMovies.

Classes
-------
AZMovies
    Manages all IMDb related interactions between the control panel
    and the application features.
"""

import logging
from threading import Thread

from content.pages.content import ContentPage


class AZMovies(Thread):
    """
    This class manages all IMDb related interactions between the control panel
    and the application features.

    Inherits from Thread class.
    """

    MOVIES = 'https://azm.to/all'
    TV_SHOWS = ''

    def __init__(self, content_url):
        super().__init__()
        self._content_url = content_url
        self.logger = logging.getLogger('scraping AZMovies')

    def run(self):
        self.logger.debug('Importing AZMovies content...')
        content = ContentPage.by_soup(self._content_url).get_content('AZMovies')

        # TODO: remove later:
        print(content[8])

        # update database here