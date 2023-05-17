from playwright.sync_api import Page

class CarsBidsResultPage: 

    def __init__(self, page: Page) -> None:
        self.page = page
        

    # check for search results on page
    def has_search_results(self) -> bool:
        result = self.page.query_selector('.hero')
        return result is not None
