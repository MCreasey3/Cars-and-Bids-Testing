import json
import pytest 

from pages.result import CarsBidsResultPage
from pages.home import CarsBidsHomePage
from pages.lowest import CarsBidsLowestPage
from pages.closest import CarsBidsClosestPage
from pages.noreserve import CarsBidsNoReservePage
from playwright.sync_api import Page


# pytest fixtures to be stored here

# handling of config file to read URL and search keywords
@pytest.fixture(scope='session')
def config():
    with open ('config.json') as config_file:
        config_data = json.load(config_file)
    return config_data


# page object fixtures

@pytest.fixture
def result_page(page: Page) -> CarsBidsResultPage:
    return CarsBidsResultPage(page)


@pytest.fixture
def home_page(page: Page) -> CarsBidsHomePage:
    return CarsBidsHomePage(page)

@pytest.fixture
def lowest_page(page: Page) -> CarsBidsLowestPage:
    return CarsBidsLowestPage(page)


@pytest.fixture
def closest_page(page: Page) -> CarsBidsClosestPage:
    return CarsBidsClosestPage(page)


@pytest.fixture
def noreserve_page(page: Page) -> CarsBidsNoReservePage:
    return CarsBidsNoReservePage