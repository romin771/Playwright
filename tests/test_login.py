from playwright.sync_api import sync_playwright
import time


def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.userlike.com/en/")

        login_button = page.locator('[data-test-id="button-to-login"]')
        login_button.click()
        login_modal = page.locator('text=Login')
        login_modal.wait_for()

        assert login_modal.is_visible(), "the element is not visible"

        email_field = page.locator("#login-username")
        email_field.clear()
        email_field.fill("romin5954@gmail.com")

        password_field = page.locator("#login-password")
        password_field.clear()
        password_field.fill("RominRomin!234!234")

        login_submitt_button = page.locator('[data-test-id="button-to-submit-login-form"]')
        login_submitt_button.click()


        dashboard_navbar = page.locator(".navbar.navbar-fixed-top.navbar-inverse")
        dashboard_navbar.wait_for()
        assert dashboard_navbar.is_visible()













        browser.close()



