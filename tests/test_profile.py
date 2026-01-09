from pages.profile_page import ProfilePage

def test_profile(page):
    profile = ProfilePage(page)
    profile.open()
    assert profile.is_loaded()
