from pages.base_page import BasePage

class CoursePage(BasePage):
    COURSE_MENU = "text=Courses"
    COURSE_LIST = ".course-card"

    def open(self):
        self.page.click(self.COURSE_MENU)
        self.page.wait_for_selector(
            self.COURSE_LIST,
            timeout=30000
        )
