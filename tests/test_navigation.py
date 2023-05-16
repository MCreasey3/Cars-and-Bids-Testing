import pytest

from pages.home import CarsBidsHomePage
from pages.lowest import CarsBidsLowestPage
from pages.closest import CarsBidsClosestPage
from pages.noreserve import CarsBidsNoReservePage

from playwright.sync_api import Page

def test_navigation_to_closest(home_page):
    home_page.navigate_closest_page()
    keywords = ["closest", "to", "me"]
    title = home_page.page.title()
    assert any(keyword.lower() in title.lower() for keyword in keywords)


def test_navigation_to_lowest(home_page):
    home_page.navigate_lowest_page()
    keywords = ["lowest", "miles"]
    title = home_page.page.title()
    assert any(keyword.lower() in title.lower() for keyword in keywords)



def test_navigation_to_noreserve(home_page):
    home_page.navigate_noreserve_page()
    keywords = ["no", "reserve"]
    title = home_page.page.title()
    assert any(keyword.lower() in title.lower() for keyword in keywords)