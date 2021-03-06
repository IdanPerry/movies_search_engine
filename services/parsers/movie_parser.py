"""
This module contains classes that represent a parsed movie or tv-show.

Classes
-------
Movie
    Represents a single parsed movie or tv-show.
"""

from abc import ABC

from services.locators import locators


class Movie(ABC):
    """
    This class represents a single parsed movie or tv-show. any other class in
    this module should inherit from this class.

    ...

    Attributes
    ----------
    parent_tag : Tag
        The HTML tag which stores the movie or tv-show.

    Methods
    -------
    name
        Returns the movie or tv-show name.
    url
        Returns an url to watch the related movie or tv-show.
    image
        Returns the movie poster image.
    """

    def __init__(self, parent_tag):
        """
        Parameters
        ----------
        parent_tag
            The tag object which stores the movie or tv-show.
        """

        self._parent_tag = parent_tag
        self._name = ''
        self._url = ''
        self._image = ''
        self._type = ''
        self._source = ''

    def __repr__(self) -> str:
        return f'{self._name} {self._url} {self._image}'

    def __eq__(self, other) -> bool:
        return self._name == other.name

    def __hash__(self) -> int:
        return hash(self._name)

    @property
    def name(self) -> str:
        """
        Returns the movie or tv-show name.
        """

        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def url(self) -> str:
        """
        Returns an url to watch the related movie or tv-show.
        """

        return self._url

    @url.setter
    def url(self, value: str):
        self._url = value

    @property
    def image(self) -> str:
        """
        Returns the movie poster image.
        """

        return self._image

    @image.setter
    def image(self, value: str):
        self._image = value

    @property
    def type(self) -> str:
        """
        Returns weather this content is a movie or tv show.
        """

        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value

    @property
    def source(self) -> str:
        """
        Returns the website's name this content came from.
        """

        return self._source

    @source.setter
    def source(self, value: str):
        self._source = value


# Inheriting classes

class SolarMovie(Movie):
    def __init__(self, parent_tag):
        super().__init__(parent_tag)
        self.name = self._parent_tag.select_one(locators.Solarmovies.NAME).string
        self.url = self._parent_tag.attrs['href'].replace('.html', '/1-1/watching.html')
        self.image = self._parent_tag.select_one(locators.Solarmovies.IMAGE).attrs['data-src']


class MoviesJoy(Movie):
    def __init__(self, parent_tag):
        super().__init__(parent_tag)
        self.name = self._parent_tag.select_one(locators.MoviesJoy.NAME).string
        self.url = f"https://moviesjoy.to{self._parent_tag.select_one(locators.MoviesJoy.LINK).attrs['href']}"
        self.image = self._parent_tag.select_one(locators.MoviesJoy.IMAGE).attrs['data-src']
