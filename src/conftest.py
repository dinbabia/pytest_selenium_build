
import re
import pytest
import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



class DriverInfo:

    stage_url = "https://omayo.blogspot.com/search?q=sdf"
    prod_url = "https://only-testing-blog.blogspot.com/2014/01/textbox.html"

    env = ""
    browser = ""  
    headless = ""
    teardown = "" 

    base_url = ""

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default= "stage", help="Test environment :[stage, prod]")
    parser.addoption("--browser", action="store", default= "chrome", help="Browsers :[chrome, firefox, edge]")
    parser.addoption("--headless", action="store_false", help="Default: [TRUE]. Type: pytest -s --headless to make it FALSE")
    parser.addoption("--teardown", action="store_false", help="Default: [TRUE]. Type: pytest -s --teardown to make it FALSE")


@pytest.fixture
def set_config(request):
    _env = request.config.getoption("--env")
    DriverInfo.env = _env

    _browser = request.config.getoption("--browser")
    DriverInfo.browser = _browser

    _headless = request.config.getoption("--headless")
    DriverInfo.headless = _headless

    _teardown = request.config.getoption("--teardown")
    DriverInfo.teardown = _teardown

    

def set_base_url(env: str):
    if env not in ["stage", "prod"]:
        raise Exception(f"[ERROR] ENVIRONMENT is invalid: {env}")
    DriverInfo.base_url = DriverInfo.stage_url if env == "stage" else DriverInfo.prod_url


@pytest.fixture
def initialize(request, set_config):

    set_base_url(env = DriverInfo.env)

    
    if DriverInfo.browser == "chrome":
        options = webdriver.ChromeOptions()

        options.headless = True if DriverInfo.headless else False
        options.add_argument("window-size=1400,600")

        download_dir = os.getcwd()
        prefs = {"download.default_directory": f"{download_dir}\\tools"}

        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        #Add this if a specific website is very slow, hence it downloads    many libraries, images and plugins. {normal, eager(interactive), none}
        c_caps = DesiredCapabilities().CHROME.copy()
        c_caps["pageLoadStrategy"] = "eager" 

        web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options, desired_capabilities=c_caps)

    elif DriverInfo.browser == "firefox":
        
        """You can change/add options for the browser here."""
        options = webdriver.FirefoxOptions()
        options.add_argument("window-size=1400,600")     
        if DriverInfo.headless:
            options.add_argument('--headless')
        download_dir = os.getcwd()

        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.helperApps.alwaysAsk.force", False)
        profile.set_preference("browser.download.dir", f"{download_dir}\\tools")
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv, application/pdf")
        profile.set_preference("pdfjs.disabled", True)
        profile.set_preference("browser.download.panel.shown", False)

        #Add this if a specific website is very slow, hence it downloads many libraries and plugins. {normal, eager(interactive), none}
        ff_caps = DesiredCapabilities().FIREFOX.copy()
        ff_caps["pageLoadStrategy"] = "normal" 
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=profile, options=options, desired_capabilities=ff_caps)

    elif DriverInfo.browser == "edge":

        """You can change/add options for the browser here."""
        options = EdgeOptions()
        options.use_chromium = True
        options.add_argument("window-size=1400,600")
        options.headless = True if DriverInfo.headless else False
        download_dir = os.getcwd()
        prefs = {
            "download.default_directory": f"{download_dir}\\tools",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True }
        options.add_experimental_option("prefs", prefs)

        #Add this if a specific website is very slow, hence it downloads many libraries and plugins. {normal, eager(interactive), none}
        e_caps = DesiredCapabilities.EDGE.copy()
        e_caps["pageLoadStrategy"] = "none"
        web_driver_path = EdgeChromiumDriverManager(log_level=20).install()
        web_driver = Edge(executable_path=web_driver_path, options=options, capabilities=e_caps)

    else:
        raise Exception (f"Driver {DriverInfo.browser} is not found")


    # Try web_driver
    try:
        web_driver.maximize_window()
        web_driver.get(DriverInfo.base_url)
    except:
        raise Exception ("[FAIL] Error on initializing")


    request.cls.driver = web_driver
    yield

    if DriverInfo.teardown: web_driver.quit()
    else: print("Driver did not exit.")



