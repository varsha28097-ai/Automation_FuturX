from pages.base_page import BasePage

class ProfilePage(BasePage):
    PROFILE_ICON = "[data-testid='profile-menu']"
    PROFILE_HEADER = "text=My Profile"

    def open(self):
        self.page.click(self.PROFILE_ICON)
        self.page.wait_for_selector(
            self.PROFILE_HEADER,
            timeout=30000
        )
