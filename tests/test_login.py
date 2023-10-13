from pages.login_page import LoginPage
import pytest
from utilities.custom_logger import configure_logger

logger = configure_logger("test_login.log" , __name__)

@pytest.mark.run(order=2)
def test_successful_login(setup_browser_page):
    page = setup_browser_page
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login("romin5954@gmail.com", "RominRomin!234!234")
    assert login_page.is_dashboard_visible(), "dashboard is not visible after login."
    logger.info("Successful login happened")




@pytest.mark.run(order=1)
def test_faild_login(setup_browser_page):
    page = setup_browser_page
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login("romin5954@gmail.com", "!234")
    assert login_page.is_login_failed(), "Login is failed , check your email and password insertion"







