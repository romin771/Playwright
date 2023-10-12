import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=400)
        context = browser.new_context()
        page = context.new_page()

        login_page = LoginPage(page)
        login_page.navigate_to_login()
        login_page.login("romin5954@gmail.com", "RominRomin!234!234")

        yield page  # Provide the logged-in page to the tests

        page.context.close()



@pytest.fixture(scope="module")
def setup_browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.userlike.com/en/")
        yield page
        page.context.close()

