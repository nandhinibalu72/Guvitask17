from .base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.profile_button="//div[@class='avatar-main-div d-flex cursor mock-interview']"
        self.logout_button= "//div[normalize-space()='Log out']"
    def logout(self):
        self.page.locator(self.profile_button).click()
        self.page.locator(self.logout_button).click()
        return True

