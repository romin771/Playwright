class WebsiteWidgetPage():
    def __init__(self, page):
        self.page = page


    def open_website_widget_page(self):
        channels_button = self.page.locator('span:has-text("Channels")').last
        channels_button.wait_for()
        channels_button.click()

        website_widget_submenu = self.page.locator("a:has-text('Website widgets')")
        website_widget_submenu.click()

    def is_website_widget_page_visible(self):
        website_widget_pagetitle = self.page.locator('h1:has-text("Website widgets")')
        website_widget_pagetitle.wait_for()
        return website_widget_pagetitle.is_visible()

    def get_website_widget_url(self):
        return self.page.url

    def add_widget(self):
        add_widget_button = self.page.locator("#widgetWizard")
        add_widget_button.click()

    def is_new_widget_modal_visible(self):
        new_widget_modal = self.page.locator("#modalWizard")
        new_widget_modal.wait_for()
        return new_widget_modal.is_visible()

    def create_widget(self):
        create_widget_button = self.page.locator(".btn.btn--large.btn-success.next")
        create_widget_button.click()

    def is_widget_created(self):
        confirm_widget_created = self.page.locator('button.btn.btn--large.configure:has-text("Copy Widget code")')
        confirm_widget_created.wait_for()
        return confirm_widget_created.is_visible()
    def close_created_widget(self):
        close_widget_button = self.page.locator(".close")
        close_widget_button.click()


