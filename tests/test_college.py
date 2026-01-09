from pages.college_page import CollegePage

def test_college_navigation(page):
    college = CollegePage(page)
    college.open()
    college.apply_location_filter("Los Angeles")
    college.select_first_college()

    assert page.url.startswith("https://dev.futurx.app")
