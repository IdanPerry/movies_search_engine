"""
This module contains classes which represent parsed content
of website pages.

To make things more simple and cleaner, the single item parsers
were separated to a different module (parsers), which is being
imported by this module.

Classes
-------
ContentPage
    Represents a website parsed content page, using either
    selenium module or requests module with BeautifulSoup class.
"""

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import requests
from bs4 import BeautifulSoup

from content.locators import imdb_locators, solar_locators
from content.parsers.imdb_item_parser import ImdbItem
from content.parsers.solar_item_parser import SolarItem

# Modify this dictionary when adding more websites to scrape from
WEBSITES = {
    'IMDb': {'locator': imdb_locators.PageContentLocators.PAGE_CONTENT, 'parser': ImdbItem},
    'Solar': {'locator': solar_locators.PageContentLocators.PAGE_CONTENT, 'parser': SolarItem}
}


class ContentPage:
    """
    Represents a website parsed page, using either selenium module
    or requests module with BeautifulSoup class.

    It is recommended that this class would be instantiated by using
    one of its class methods:
    ContentPage.by_soup(page_url)
    ContentPage.by_selenium(page_url)

    ...

    Attributes
    ----------
    source
        The source from which to parse the web page.
        Source could be either a BeautifulSoup object or one of
        the selenium webdriver objects (for example Chrome).

    Methods
    -------
    get_content(website=str)
        Returns a list of Item objects.
    """

    def __init__(self, source):
        """
        Parameters
        ----------
        source
            The source from which to parse the web page.
        """

        self._source = source
        _method = ''

    @classmethod
    def by_soup(cls, page_url=str):
        """
        Parses the target page using requests and BeautifulSoup.

        Parameters
        ----------
        page_url : str
            The url from which to parse the page.

        Returns
        -------
        ContentPage
            Instance of this class.
        """

        _method = 'soup'
        _page = requests.get(page_url).content
        _source = BeautifulSoup(_page, 'html.parser')

        return cls(_source)

    @classmethod
    def by_selenium(cls, driver, page_url=str):
        """
        Parses the target page using selenium webdriver.

        Parameters
        ----------
        page_url : str
            The url from which to parse the page.
        driver : Chrome
            The selenium webdriver object.

        Returns
        -------
        ContentPage
            Instance of this class.
        """

        driver.get(page_url)

        return cls(driver)

    def _scroll_page(self):
        scroll_pause = 1

        current_height = self._source.execute_script('return document.body.scrollHeight')

        # scroll to bottom
        while True:
            self._source.execute_script('window.scrollTo(0, document.body.scrollHeight)')

            time.sleep(scroll_pause)
            new_height = self._source.execute_script('return document.body.scrollHeight')
            if current_height == new_height:
                break

            current_height = new_height

    def get_content(self, name=str, method=str) -> list:
        """
        Parses the page represented by this class and
        returns a list of Item objects.

        Parameters
        ----------
        name : str
            The website name from which to parse the page.
        method : str
            The module by which to use: BeautifulSoup or Selenium.

        Returns
        -------
        list
            A list of Item objects from the parsed page.
        """

        _items_list = None

        if method == 'soup':
            _items_list = self._source.select(WEBSITES[name]['locator'])
        elif method == 'selenium':
            _items_list = self._source.find_element_by_css_selector(WEBSITES[name]['locator'])

        return [WEBSITES[name]['parser'](i) for i in _items_list]
