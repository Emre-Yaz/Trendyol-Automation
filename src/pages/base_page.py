from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.close_popup_button = page.get_by_title("Kapat", exact=True).get_by_role("img")
        self.reject_all_button = page.get_by_role("button", name="Tümünü Reddet")


    def close_cookies_popup(self):
        self.close_popup_button.click()
        self.reject_all_button.click()

    def click_element(self, locator: str):
        self.page.locator(locator).click()

    def get_text(self, locator: str):
        return self.page.locator(locator).inner_text()

    def fill_input(self, locator: str, value: str):
        self.page.locator(locator).fill(value)

    def wait_for_element(self, locator: str, timeout: int = 3000):
        self.page.locator(locator).wait_for(timeout=timeout)

    def log_action(self, action: str):
        print(f"Performing action: {action}")

    def click_button(self, button_name: str):
        self.page.locator(f'button:has-text("{button_name}")').click()

    def assert_text_visible(self, text: str):
        assert self.page.locator(f"text={text}").is_visible()

    def assert_element_visible(self, locator: str):
        assert self.page.locator(locator).is_visible()


