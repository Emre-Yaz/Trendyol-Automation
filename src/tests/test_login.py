from playwright.sync_api import Page
from src.pages.login_page import LoginPage
from src.tests.base_test import BaseTest
from src.pages.base_page import BasePage


class TestLogin(BaseTest):

    def test_successful_login(self, page: Page):
        self.go_to_site()
        base_page = BasePage(page)
        base_page.close_cookies_popup()
        login_page = LoginPage(page)
        login_page.login_with_valid_credentials()
        assert login_page.is_login_successful(
        ), "logged_in_check locator could not be found on the current page"

    # def test_login_with_invalid_email(self, page: Page):
    #     self.go_to_site()
    #     base_page = BasePage(page)
    #     base_page.close_cookies_popup()
    #     login_page = LoginPage(page)
    #     login_page.login_with_invalid_email()
    #     assert login_page.is_login_successful() == False, "Expected not to be logged in"
    #     assert login_page.is_invalid_email_message_seen(
    #     ), "Expected to see invalid email message"

    # # I guess they had a precaution to prevent users from trying wrong passwords with automation.
    # # The behaviour while manually testing and the automation tests are different.
    # def test_login_with_invalid_password(self, page: Page):
    #     self.go_to_site()
    #     base_page = BasePage(page)
    #     base_page.close_cookies_popup()
    #     login_page = LoginPage(page)
    #     login_page.login_with_invalid_password()
    #     assert login_page.is_login_successful() == False, "Expected not to be logged in"
    #     assert login_page.is_invalid_password_message_seen(
    #     ), "Expected to see invalid password message"
