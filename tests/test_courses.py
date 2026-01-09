from pages.course_page import CoursePage

def test_course_navigation(page):
    course = CoursePage(page)
    course.open()
    course.apply_stream_filter("Engineering")
    course.open_first_course()

    assert page.url.startswith("https://dev.futurx.app")
