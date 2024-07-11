from PageActions.page import Page
from selenium.webdriver.common.by import By


class LoginPageActions(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def go_to_facebook_page(self):
        self.navigation.go_to_page("https://facebook.com")

    def enter_email(self, text: str):
        locator = (By.ID, "email")
        self.interaction.send_keys(locator, text)

    def enter_password(self, text: str):
        locator = (By.ID, "pass")
        self.interaction.send_keys(locator, text)

    def click_login_button(self):
        locator = (By.NAME, "login")
        self.interaction.click(locator)

