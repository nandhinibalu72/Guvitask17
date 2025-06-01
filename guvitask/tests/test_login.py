from time import sleep

import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.mark.parametrize("username, password, expected", [
    ("nandhinibalu72@gmail.com", "Nivan@10", True),
    ("invaid_user", "sdfgd", False)
])
def test_login_functionality(page, username, password, expected):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    
    login_page.load("https://v2.zenclass.in/")
    login_page.login(username, password)

    if expected:
        assert login_page.is_login_successful(), "Login should be successful, but it failed"
        assert dashboard_page.logout(), "Logout should be successful, but it failed"
    else:
        error_message = login_page.get_error_message()
        assert error_message is not None and error_message != "", "Expected error message for invalid login, but got none"
def test_input_boxes_and_submit_button(page):
    login_page = LoginPage(page)
    login_page.load("https://v2.zenclass.in/")
    sleep(10)
    assert page.locator(login_page.username_input).is_visible(), "Username field is not visible"
    assert page.locator(login_page.password_input).is_visible(), "Password field is not visible"
    assert page.locator(login_page.login_button).is_enabled(), "Submit button is not enabled"

