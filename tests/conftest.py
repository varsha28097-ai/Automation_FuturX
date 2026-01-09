import pytest
from playwright.sync_api import sync_playwright

DEV_URL = "https://dev.futurx.app"

@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(
            storage_state="auth_state.json"
        )

        yield context
        context.close()
        browser.close()

@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    page.goto(DEV_URL)
    return page
