"""
This module contains classes that represent a parsed movie
or tv-show from Solarmovies website.

Classes
-------
NetflixItem
    Represents a single parsed movie or tv-show from Solarmovies website,
    allowing the user to observe its properties (tv-show name, movie rating etc.)
"""

from content.locators.solar_locators import ItemLocators


class SolarItem:
    """
    This class represents a single parsed movie or tv-show from Solarmovies website,
    allowing the user to observe its properties (tv-show name, movie watch link etc.)

    ...

    Attributes
    ----------
    item : Tag
        The HTML tag which stores the movie or tv-show.

    Methods
    -------
    name
        Returns the contents name.
    link
        Returns a link to watch the related movie or tv-show.
    """

    def __init__(self, item):
        """
        Parameters
        ----------
        item
            The tag object which stores the movie or tv-show.
        """

        self._item = item

    def __repr__(self):
        return f'{self.name} {self.link}'

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    @property
    def name(self):
        """
        Parses this object tag attribute which represents a movie or tv-show
        and returns its name as a string.
        """

        return self._item.select_one(ItemLocators.NAME).string

    @property
    def link(self):
        """
        Parses this object tag attribute which represents a movie or tv-show
        and returns a Solarmovies watch link.
        """

        return self._item.attrs[ItemLocators.LINK]
