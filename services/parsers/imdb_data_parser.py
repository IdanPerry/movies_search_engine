"""
This module contains classes that represent a parsed movie
or tv-show from IMDb website.

Classes
-------
ImdbItem
    Represents a single parsed movie or tv-show from IMDb website,
    allowing the user to observe its properties (tv-show name, movie rating etc.)
"""

import requests
import re
from bs4 import BeautifulSoup

from services.locators.locators import IMDb


class ImdbItem:
    """
    This class represents a single parsed movie or tv-show from IMDb website,
    allowing the user to observe its attributes (tv-show name, movie rating etc.)

    Since IMDb is mostly static website, this class make use of
    requests module together with BeautifulSoup class to parse
    the pages content.

    ...

    Attributes
    ----------
    parent_tag : Tag
        The HTML tag which stores the movie or tv-show.

    Methods
    -------
    name
        Returns the contents name.
    year
        Returns the contents year as string.
    rating
        Returns the contents rating as string.
    trailer
        Returns a trailer url to the related content.
    seasons
        Returns the tv-show number of seasons as string.
    actors
        Returns a string representation of the stars actors
        of the related content.
    description
        Returns a description of the content as a string.
    """

    def __init__(self, parent_tag):
        """
        Parameters
        ----------
        parent_tag
            The tag object which stores the movie or tv-show.
        """

        self._parent_tag = parent_tag

    def __repr__(self):
        return f'{self.name} {self.year} {self.rating}\n{self.actors}\n{self.description}\n'

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    @property
    def name(self) -> str:
        """
        Parses this object tag attribute which represents a movie or tv-show
        and returns its name as a string.
        """

        name = self._parent_tag.select_one(IMDb.NAME).string

        if name is None:
            return ' '

        return name

    @property
    def year(self) -> str:
        """
        Parses this object tag attribute which represents a movie or tv-show
        and returns its year as a string.

        Raises
        ------
        AttributeError
            If the related content doesn't have a year.
        ValueError
            If the selected string doesn't represent an int.

        TypeError
            If there is type mismatch in sub method.
        """

        try:
            content = self._parent_tag.select_one(IMDb.YEAR).string
            year = re.sub(r'[()]', '', content)
            # check if year represents an int
            int(year)
            return year

        except (AttributeError, ValueError, TypeError):
            return '0'

    @property
    def rating(self) -> str:
        """
        Parses this object tag attribute which represents a movie or tv-show
        and returns its rating as a string.

        Raises
        ------
        AttributeError
            If the related content doesn't have a rating.

        ValueError
            If the selected string doesn't represent an int.
        """

        try:
            rating = self._parent_tag.select_one(IMDb.RATING).string
            # check if rating represents a float
            float(rating)
            return rating

        except (AttributeError, ValueError):
            return '0.0'

    @property
    def trailer(self) -> str:
        """
        Parses this object tag attribute which represents a movie or tv-show
        and returns an IMDb watch trailer url.
        """

        trailer = f"http://imdb.com{self._parent_tag.select_one(IMDb.TRAILER).attrs['href']}"

        if trailer is None:
            return ' '

        return trailer

    @property
    def seasons(self) -> str:
        """
        Parses this object tag attribute which represents a tv-show
        and returns its number of seasons as string.

        Raises
        ------
        AttributeError
            If the related content is a movie or doesn't specify
            the number of seasons.

        ValueError
            If the selected string doesn't represent an int.
        """

        try:
            # TODO: significantly slows down the program, don't use it
            page = requests.get(self.trailer).content
            content = BeautifulSoup(page, 'html.parser').select_one(IMDb.SEASONS).string
            seasons = re.sub(' seasons', '', content)
            # check if seasons represents an int
            int(seasons)
            return seasons

        except (AttributeError, ValueError):
            return '0'

    @property
    def actors(self) -> str:
        """
        Parses this object tag attribute which represents a movie or tv-show
        and returns a string representation of it's stars actors.
        """

        actors = [actor.string for actor in self._parent_tag.select(IMDb.ACTORS)]

        if actors is None:
            return ' '

        return ', '.join(actors)

    @property
    def description(self) -> str:
        """
        Parses this object tag attribute which represents a movie or tv-show
        and returns its description as a string.

        Since every movie description in IMDb starts with a white new line,
        the method strip() is being invoked on the returned string.
        """

        try:
            description = self._parent_tag.select_one(IMDb.DESCRIPTION).string

            if description is None:
                return ' '

            return description.strip()

        except AttributeError:
            return ' '
