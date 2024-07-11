
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager



class Browser:

    def __init__(self, name, environment):
        self.name = name
        self.environment = environment
        self.base_url = EnvironmentInformation.get_base_url(environment)

    def build_browser(self, driver_options):
        if self.name == "chrome":
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=driver_options)
        elif self.name == "firefox":
            self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=driver_options)

    def exit_browser(self):
        self.driver.quit()

class EnvironmentInformation:
    @staticmethod
    def get_base_url(environment):
        base_urls = {
            "stage": "https://staging.example.com",
            "prod": "https://production.example.com"
        }
        return base_urls.get(environment, "https://default.com")


