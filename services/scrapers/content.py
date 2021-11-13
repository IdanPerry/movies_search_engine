"""
This module contains classes which represent parsed content
of website pages.

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
from aiohttp import ClientSession
import asyncio

from services.locators import locators
from services.parsers.imdb_data_parser import ImdbItem
from services.parsers.movie_parser import SolarMovie, MoviesJoy

# Modify this dictionary when adding more websites to scrape from.
WEBSITES = {
    'IMDb': {'locator': locators.IMDb.PAGE_CONTENT, 'parser': ImdbItem},
    'Solar': {'locator': locators.Solarmovies.PAGE_CONTENT, 'parser': SolarMovie},
    'MoviesJoy': {'locator': locators.MoviesJoy.PAGE_CONTENT, 'parser': MoviesJoy}
}


class ContentPage:
    """
    Represents a website parsed page, using either selenium module
    or BeautifulSoup.

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

    @classmethod
    def by_soup(cls, urls: list):
        """
        Parses the target page using requests and BeautifulSoup.

        Parameters
        ----------
        urls : list
            List of the urls from which to parse the pages.

        Returns
        -------
        ContentPage
            Instance of this class.
        """

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        # all HTML pages
        pages = loop.run_until_complete(ContentPage._fetch_all_pages(loop, urls))

        return cls(pages)

    @classmethod
    def by_selenium(cls, driver, page_url: str):
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

    @staticmethod
    async def _fetch_page(session, url):
        async with session.get(url) as response:
            return await response.text()

    @staticmethod
    async def _fetch_all_pages(loop, urls):
        async with ClientSession(loop=loop) as session:
            tasks = [ContentPage._fetch_page(session, url) for url in urls]
            return await asyncio.gather(*tasks)

    def _scroll_page(self) -> None:
        # Scrolls dynamic pages

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

    def get_content(self, name: str, method: str) -> list:
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

        # list of HTML tags
        _content_list = []

        if method == 'soup':
            # self._source == all html pages
            for page in self._source:
                _content_list.extend(BeautifulSoup(page, 'html.parser').select(WEBSITES[name]['locator']))
            
        elif method == 'selenium':
            _content_list = self._source.find_element_by_css_selector(WEBSITES[name]['locator'])

        # WEBSITES[name]['parser'] is instance of Movie class
        return [WEBSITES[name]['parser'](content) for content in _content_list]
