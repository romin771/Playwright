from playwright.sync_api import ElementHandle

def assert_element_visible(element: ElementHandle):
    assert element.is_visible(), f"Element {element.locator} is not visible."

def assert_element_enabled(element: ElementHandle):
    assert element.is_enabled(), f"Element is not enabled: {element.locator}"

def assert_element_text_equal(element: ElementHandle, expected_text: str):
    assert element.inner_text() == expected_text, f"Expected text '{expected_text}' but got '{element.inner_text()}'"

def assert_element_text_contains(element: ElementHandle, expected_text: str):
    actual_text = element.inner_text()
    assert expected_text in actual_text, f"Expected text '{expected_text}' not found in '{actual_text}'"

def assert_element_has_attribute(element: ElementHandle, attribute_name: str, expected_value: str):
    actual_value = element.get_attribute(attribute_name)
    assert actual_value == expected_value, f"Attribute '{attribute_name}' has value '{actual_value}' but expected '{expected_value}'"
def assert_element_has_class(element: ElementHandle, class_name: str):
    assert class_name in element.get_attribute("class"), f"Element does not have class '{class_name}'"