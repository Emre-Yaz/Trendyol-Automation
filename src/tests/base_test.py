import pytest
from playwright.sync_api import Page

class BaseTest:
    # In python, no __init__ is needed for a test class. In fact, it will raise an error.
    # Instead use setup() fixture.
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Automatically set up the Playwright page for all tests."""
        self.page = page

    def go_to_site(self):
        self.page.goto("https://www.trendyol.com/")

    def capture_screenshot(self, test_name: str):
        screenshot_path = f"reports/screenshots/{test_name}.png"
        self.page.screenshot(path=screenshot_path)

    def tear_down(self):
        if self.page:
            self.page.close()
