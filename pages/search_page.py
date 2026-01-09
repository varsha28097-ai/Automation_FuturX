from pages.base_page import BasePage

class SearchPage(BasePage):
    SEARCH_INPUT = "input[placeholder='Search']"

    def open(self):
        self.page.click("text=Search")
        self.page.wait_for_selector(
            self.SEARCH_INPUT,
            timeout=15000
        )
