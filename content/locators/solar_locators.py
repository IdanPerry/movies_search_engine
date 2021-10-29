"""
This module contains classes with constants only, to locate
and select HTML elements inside Solarmovie website pages.

Classes
-------
PageContentLocators :
    Includes constants to select a list of HTML elements,
    grouped together to store a list of movies or tv-shows.

ItemLocators :
    Includes constants to select an HTML element that
    stores a single attribute of the related movie or tv-shows.
"""


class PageContentLocators:
    """
    This class includes constants to select a list of HTML elements,
    grouped together to store a list of movies or tv-shows.
    """

    PAGE_CONTENT = 'div[class="movies-list movies-list-full"] a'


class ItemLocators:
    """
    This class includes constants to select an HTML element that
    stores a single attribute of the related movie or tv-shows.
    """

    PARENT = 'span'
    NAME = 'a div.mli-info h2'
    LINK = 'href'
