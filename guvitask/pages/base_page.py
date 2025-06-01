from playwright.sync_api import Page, expect, TimeoutError

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def wait_for_element(self, selector, timeout=5000):
        try:
            return self.page.wait_for_selector(selector, timeout=timeout)
        except TimeoutError:
            raise Exception(f"Element '{selector}' not found within timeout.")
