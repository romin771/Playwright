from pages.login_page import LoginPage
from pages.website_widget_page import WebsiteWidgetPage
import pytest

@pytest.mark.run(order=1)
def test_add_widget(setup_browser_page):
    page = setup_browser_page
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login("romin5954@gmail.com", "RominRomin!234!234")

    website_widget_page = WebsiteWidgetPage(page)
    website_widget_page.open_website_widget_page()
    assert website_widget_page.is_website_widget_page_visible()
    assert "um_widget" in website_widget_page.get_website_widget_url()

    website_widget_page.add_widget()
    assert website_widget_page.is_new_widget_modal_visible()

    website_widget_page.create_widget()
    assert website_widget_page.is_widget_created()
    website_widget_page.close_created_widget()


@pytest.mark.run(order=2)
def test_remove_last_added_widget(setup_browser_page):
    page = setup_browser_page
    widget_row = page.locator("tbody")
    widget_row.wait_for()
    widget_row_numbers = widget_row.locator("tr").count()
    if widget_row_numbers >= 2:
        last_created_widget_row = widget_row.locator("tr").nth(0)
        delete_button = last_created_widget_row.locator('[data-original-title="Delete Widget"]')
        delete_button.click()
        confirm_delete_button = page.locator(".btn.btn-danger.btn--large")
        confirm_delete_button.wait_for()
        confirm_delete_button.click()
    else:
        print("Only the Default widget is available ")
























