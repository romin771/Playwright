from playwright.sync_api import Page
from playwright.sync_api import ElementHandle

def scroll_page_up(page: Page):
    page.evaluate("window.scrollTo(0, 0)")

def scroll_page_down(page: Page):
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

def scroll_to_element(page: Page, element: ElementHandle):
    element.scroll_into_view()

def bring_page_to_front(page: Page):
    page.bring_to_front()