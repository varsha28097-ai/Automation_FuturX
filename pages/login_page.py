from pages.base_page import BasePage

class LoginPage(BasePage):
    DASHBOARD_INDICATOR = "text=Dashboard"

    def open(self):
        self.goto("https://dev.futurx.app")

    def wait_for_dashboard(self):
        self.page.wait_for_selector(
            self.DASHBOARD_INDICATOR,
            timeout=30000
        )
