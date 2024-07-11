from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NavigationHandler:
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self, page):
        self.driver.get(page)

class Handler:

    def __init__(self, driver, explicitly_wait=10):
        self._wait = WebDriverWait(driver, explicitly_wait)

class InteractionHandler(Handler):

    def __init__(self, driver):
        super().__init__(driver)

    def send_keys(self, by_locator, text):
        self._wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def click(self, by_locator):
        self._wait.until(EC.visibility_of_element_located(by_locator)).click()

class WaitHandler(Handler):

    def __init__(self, driver):
        super().__init__(driver)

