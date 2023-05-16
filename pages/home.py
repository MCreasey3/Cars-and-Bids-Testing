import json
from playwright.sync_api import Page

class CarsBidsHomePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.load_config()
        self.search_input = self.page.locator('input.form-control[name="search"]')
        


    def load_config(self):
        with open('config.json') as config_file:
            config_data = json.load(config_file)
            self.URL = config_data['URL']
            self.search_keywords = config_data['search_keywords']
            # return config_data['search_keywords']
    

    def load(self) -> None:
        self.page.goto(self.URL)

    
    def search(self, keyword: str) -> None:
        self.search_input.fill(keyword)
        self.search_input.press("Enter")
        #self.page.wait_for_navigation()
        


