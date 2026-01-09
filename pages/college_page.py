from pages.base_page import BasePage

class CollegePage(BasePage):
    COLLEGE_MENU = "text=Colleges"
    COLLEGE_HEADER = "h1"

    def open(self):
        self.page.click(self.COLLEGE_MENU)
        self.page.wait_for_selector(
            self.COLLEGE_HEADER,
            timeout=30000
        )
