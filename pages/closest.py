from playwright.sync_api import Page

class CarsBidsClosestPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    
    # get page title as string and return to test for indicated word
    def get_page_title(self) -> str:
        return self.page.title()