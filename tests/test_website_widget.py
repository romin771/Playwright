from pages.website_widget_page import WebsiteWidgetPage
import pytest
from utilities.custom_assersions import assert_element_text_equal


@pytest.mark.run(order=3)
def test_add_widget(browser):
    page = browser
    website_widget_page = WebsiteWidgetPage(page)
    website_widget_page.open_website_widget_page()
    assert website_widget_page.is_website_widget_page_visible()
    assert "um_widget" in website_widget_page.get_website_widget_url()

    # from util/custom_assert
    assert_element_text_equal(website_widget_page.get_add_widget_button(), " Add Widget")

    website_widget_page.add_widget()
    assert website_widget_page.is_new_widget_modal_visible()

    website_widget_page.create_widget()
    assert website_widget_page.is_widget_created()
    website_widget_page.close_created_widget()


@pytest.mark.run(order=4)
def test_remove_last_added_widget(browser):
    page = browser
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

























