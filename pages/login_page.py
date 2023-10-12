class LoginPage:

    def __init__(self, page):
        self.page = page

    def navigate_to_login(self):

        self.page.goto("https://www.userlike.com/en/")
        login_button = self.page.locator('[data-test-id="button-to-login"]')
        login_button.click()
        login_modal = self.page.locator('text=Login')
        login_modal.wait_for()
        assert login_modal.is_visible(), "Login modal is not visible."

    def login(self, email, password):
        email_field = self.page.locator("#login-username")
        email_field.clear()
        email_field.fill(email)

        password_field = self.page.locator("#login-password")
        password_field.clear()
        password_field.fill(password)

        login_submit_button = self.page.locator('[data-test-id="button-to-submit-login-form"]')
        login_submit_button.click()

    def is_dashboard_visible(self):
        dashboard_navbar = self.page.locator(".navbar.navbar-fixed-top.navbar-inverse")
        dashboard_navbar.wait_for()
        return dashboard_navbar.is_visible()



