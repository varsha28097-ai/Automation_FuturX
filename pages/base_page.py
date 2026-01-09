class BasePage:
    def __init__(self, page):
        self.page = page

    def wait_after_navigation(self):
        # waits until page is fully loaded (max 15s)
        self.page.wait_for_load_state("networkidle", timeout=30000)

    def goto(self, url):
        self.page.goto(url, timeout=30000)
        self.wait_after_navigation()
