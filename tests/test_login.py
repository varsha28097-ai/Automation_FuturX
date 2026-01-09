from pages.login_page import LoginPage

EMAIL = "varsha28097@gmail.com"
PASSWORD = "Varsha0328@btsot7130697"

def test_login(page):
    login = LoginPage(page)
    login.open()
    login.login(EMAIL, PASSWORD)

    # assertion after successful login
    assert "dashboard" in page.url or "home" in page.url
