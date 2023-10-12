from pages.login_page import LoginPage
import pytest

def test_successful_login(setup_browser_page):
    page = setup_browser_page
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login("romin5954@gmail.com", "RominRomin!234!234")
    assert login_page.is_dashboard_visible(), "dashboard is not visible after login."




