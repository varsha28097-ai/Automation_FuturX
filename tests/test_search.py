from pages.search_page import SearchPage

def test_search(page):
    search = SearchPage(page)
    search.open()
    search.search("automation")

    page.wait_for_timeout(100000)
    assert page.url.startswith("https://dev.futurx.app")
