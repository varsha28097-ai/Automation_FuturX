from ..pages.login_page import LoginPage
from ..pages.college_page import CollegePage
from ..pages.course_page import CoursePage
from ..pages.search_page import SearchPage
from ..pages.profile_page import ProfilePage

def test_dashboard_navigation(page):
    login = LoginPage(page)
    login.open()
    login.wait_for_dashboard()

    college = CollegePage(page)
    college.open()

    course = CoursePage(page)
    course.open()

    search = SearchPage(page)
    search.open()

    profile = ProfilePage(page)
    profile.open()
