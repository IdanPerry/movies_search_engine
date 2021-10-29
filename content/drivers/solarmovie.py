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
from content import views


class Solarmovie(Thread):
    """
    This class manages Solarmovie related content, which includes scraping the content
    and writing it to the related database using the views model.

    Inherits from Thread class.
    """

    CONTENT = {
        'movies': {'content_type': 'movie',
                   'link': 'https://www2.solarmovie.to/movie/filter/movies.html'},
        'tv-shows': {'content_type': 'tv-show',
                     'link': ''}
    }

    def __init__(self, content):
        super().__init__()
        self._content = content
        self.logger = logging.getLogger('scraping Solarmovie')

    def run(self):
        self.logger.debug('Importing Solarmovie content...')
        content = ContentPage.by_soup(self._content['link']).get_content('Solar', 'soup')
        content.sort()

        for item in content:
            views.insert_show(item, 'Solarmovie', self._content['content_type'])
