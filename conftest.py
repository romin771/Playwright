import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="package")
def setup_browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.context.close()