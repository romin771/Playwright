from playwright.sync_api import Page

class BrowserUtils:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_url(self, url: str):
        self.page.goto(url)

    def fill_input_field(self, selector: str, value: str):
        input_field = self.page.locator(selector)
        input_field.fill(value)

    def navigate_back(self):
        self.page.goBack()

    def navigate_forward(self):
        self.page.goForward()


    # for iframe
    def switch_to_frame(page: Page, frame_selector):
        frame = page.locator(frame_selector).first
        page.frame_element(frame)

    def switch_to_default_content(page: Page):
        page.frame_element(None)