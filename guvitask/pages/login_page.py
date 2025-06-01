from time import sleep
from pages.base_page import BasePage
from playwright.sync_api import expect, TimeoutError

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = "//input[@id=':r0:']"
        self.password_input = "//input[@id=':r1:']"
        self.login_button = "//button[@type='submit']"
        self.profile_button = "//*[@id='profile-click-icon']"
        self.error_msg = "//*[@id=':r1:-helper-text']"  # update if needed
        self.logout = "//*[@id='root']/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div[4]/div[3]"

    def load(self, url):
        self.page.goto(url)

    def login(self, username, password):
        expect(self.page.locator(self.username_input)).to_be_visible(timeout=10000)
        expect(self.page.locator(self.password_input)).to_be_visible()
        self.page.locator(self.username_input).fill(username)
        self.page.locator(self.password_input).fill(password)
        self.page.locator(self.login_button).click()
        try:
            close_button = self.page.locator("//button[@class='custom-close-button']")
            close_button.click(timeout=3000)
            print("INFO: Closed the popup using close button.")
        except TimeoutError:
            print("INFO: No popup appeared, continuing normally.")

    def is_login_successful(self):
        try:
            self.page.wait_for_selector(self.profile_button, timeout=10000)
            return True
        except:
            self.page.screenshot(path="login_failed.png")
            return False

    def get_error_message(self):
        try:
            self.page.wait_for_selector(self.error_msg, timeout=50000)
            return self.page.locator(self.error_msg).inner_text()
        except:
            return "Error message not found"
