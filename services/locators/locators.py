"""
This module contains classes with constants only, to locate
and select HTML elements.
"""


class IMDb:
    PAGE_CONTENT = 'div.lister-item-content'
    NAME = 'a'
    YEAR = 'span[class^="lister-item-year"]'
    RATING = 'div[name="ir"] strong'
    TRAILER = 'a'
    SEASONS = 'label.ipc-simple-select__label'
    DESCRIPTION = 'p ~ .text-muted'
    ACTORS = 'p ~ p ~ p a'


class Solarmovies:
    PAGE_CONTENT = 'div[class="movies-list movies-list-full"] a'
    PARENT = 'span'
    NAME = 'a div.mli-info h2'
    LINK = ''
    IMAGE = 'img'


class MoviesJoy:
    PAGE_CONTENT = 'div[class="flw-item"]'
    NAME = 'h2 a'
    LINK = 'div.film-poster a'
    IMAGE = 'div.film-poster img'


