import json
from pathlib import Path
from playwright.sync_api import expect
from src.pages.base_page import BasePage


class LoginPage(BasePage):
    data_path = Path(__file__).parent.parent / "test_data" / "login_data.json"
    with open(data_path, "r") as f:
        credentials = json.load(f)

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.login_paragraph = page.get_by_role(
            "paragraph").filter(has_text="Giriş Yap")
        self.email_input = page.get_by_test_id("email-input")
        self.password_input = page.get_by_test_id("password-input")
        self.login_button = page.locator(
            "form").get_by_role("button", name="Giriş Yap")
        # if we are sure that the text is unique, we can use get_by_text.
        self.invalid_login_message = page.locator("#error-box-wrapper")

    def login(self, email: str, password: str):
        self.login_paragraph.click()
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def login_with_valid_credentials(self):
        creds = self.credentials["valid_credentials"]
        self.login(creds["email"], creds["password"])

    def login_with_invalid_password(self):
        creds = self.credentials["invalid_password"]
        self.login(creds["email"], creds["password"])

    def login_with_invalid_email(self):
        creds = self.credentials["invalid_email"]
        self.login(creds["email"], creds["password"])

    def is_login_successful(self):
        return self.login_paragraph.is_visible() == False

    def is_invalid_email_message_seen(self):
        try:
            self.invalid_login_message.wait_for(state="visible", timeout=10000)
            visible = self.invalid_login_message.is_visible()
            text = self.invalid_login_message.inner_text()
            return visible and ("Lütfen geçerli bir e-posta" in text)
        except Exception as e:
            print(f"Error checking invalid email message: {e}")
            return False

    def is_invalid_password_message_seen(self):
        try:
            self.invalid_login_message.wait_for(state="visible", timeout=50000)
            visible = self.invalid_login_message.is_visible()
            text = self.invalid_login_message.inner_text()
            return visible and ("E-posta adresiniz ve/veya" in text)
        except Exception as e:

            print(f"Error checking invalid password message: {e}")
            return False
