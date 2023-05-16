import pytest
import json

from pages.home import CarsBidsHomePage
from pages.result import CarsBidsResultPage
from playwright.sync_api import Page


def load_search_keywords():
    with open('config.json') as file:
        config_data = json.load(file)
    return config_data['search_keywords']


def test_carsbids_search(page, home_page, result_page):

    search_keywords = load_search_keywords()

    for keyword in search_keywords:
        # load initial page
        home_page.load()
        # search using keyword
        home_page.search(keyword)
        # assert results > 0
        assert result_page.has_search_results(), "No search results found."




