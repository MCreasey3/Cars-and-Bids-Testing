import json
from playwright.sync_api import Page

class CarsBidsHomePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.load_config()
        self.search_input = self.page.locator('input.form-control[name="search"]')
        

    # load config file to get URL and keywords for testing
    def load_config(self):
        with open('config.json') as config_file:
            config_data = json.load(config_file)
            self.URL = config_data['URL']
            self.search_keywords = config_data['search_keywords']
            # return config_data['search_keywords']
    

    # load the landing page
    def load(self) -> None:
        self.page.goto(self.URL)

    
    # fill search bar and proceed to results page by pressing Enter key
    # site does not currently have a search button icon to click
    def search(self, keyword: str) -> None:
        self.search_input.fill(keyword)
        self.search_input.press("Enter")
    

    # load home page and click link for 'Closest to Me' page
    def navigate_closest_page(CarsBidsHomePage):
        # Load home page first
        CarsBidsHomePage.load()
        # Click link for 'Closest to Me' page
        CarsBidsHomePage.page.click('a[href="/?sort=closest"]')

    
    # load home page and click link for 'Lowest Mileage' page
    def navigate_lowest_page(CarsBidsHomePage):
        # Load home page first
        CarsBidsHomePage.load()
        # Click link for 'Lowest Mileage' page
        CarsBidsHomePage.page.click('a[href="/?sort=lowest_mileage"]')

    
    # load home page and click link for 'No Reserve' page
    def navigate_noreserve_page(CarsBidsHomePage):
        # Load home page first
        CarsBidsHomePage.load()
        # Click link for 'No Reserve' page
        CarsBidsHomePage.page.click('a[href="/?sort=no_reserve"]')
        


