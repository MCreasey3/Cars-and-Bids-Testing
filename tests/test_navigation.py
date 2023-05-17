import pytest

from pages.home import CarsBidsHomePage
from pages.lowest import CarsBidsLowestPage
from pages.closest import CarsBidsClosestPage
from pages.noreserve import CarsBidsNoReservePage

from playwright.sync_api import Page


# verify navigation to 'Closest to Me' page
def test_navigation_to_closest(home_page):
    home_page.navigate_closest_page()
    keywords = ["closest", "to", "me"]
    title = home_page.page.title()
    # check for keywords in page title
    assert any(keyword.lower() in title.lower() for keyword in keywords)


# verify navigation for 'Lowest Mileage' page
def test_navigation_to_lowest(home_page):
    home_page.navigate_lowest_page()
    keywords = ["lowest", "miles"]
    title = home_page.page.title()
    # check for keywords in page title
    assert any(keyword.lower() in title.lower() for keyword in keywords)


# verify navigation for 'No Reserve' page
def test_navigation_to_noreserve(home_page):
    home_page.navigate_noreserve_page()
    keywords = ["no", "reserve"]
    title = home_page.page.title()
    # check for keywords in page title
    assert any(keyword.lower() in title.lower() for keyword in keywords)