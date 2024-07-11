
from selenium import webdriver


class SelectDriverOptions:
    def __init__(self, browser_name):
        self.opts = self._select_options(browser_name)

    def _select_options(self, browser_name):
        if browser_name == "chrome":
            return webdriver.ChromeOptions()
        elif browser_name == "firefox":
            return webdriver.FirefoxOptions()

class ChromeDriverOptions:

    def __init__(self, chrome_driver: SelectDriverOptions):
        self.options = chrome_driver
        self._set_default_options()

    def set_to_headless(self):
        self.options.add_argument('--headless')

    def _set_default_options(self):
        self.options.add_experimental_option("detach", True)

class FirefoxDriverOptions:

    def __init__(self, firefox_driver: SelectDriverOptions):
        self.options = firefox_driver

    def set_to_headless(self):
        self.options.add_argument('--headless')


