"""
This module contains classes with constants only, to locate
and select HTML elements inside IMDb pages.

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

    PAGE_CONTENT = 'div.lister-item-content'


class ItemLocators:
    """
    This class includes constants to select an HTML element that
    stores a single attribute of the related movie or tv-shows.
    """

    NAME = 'a'
    YEAR = 'span[class^="lister-item-year"]'
    RATING = 'div[name="ir"] strong'
    TRAILER = 'a'
    SEASONS = 'label.ipc-simple-select__label'
    DESCRIPTION = 'p ~ .text-muted'
    ACTORS = 'p ~ p ~ p a'
