import pytest

from driver import Browser 
from driver_profiles import ProfileOneDriverOptions, ProfileTwoDriverOptions

@pytest.fixture(scope="session")
def browser(start_session):
    browser_name = start_session[0]
    environment = start_session[1]
    profile = start_session[2]

    if profile == "clean":
        opts = ProfileOneDriverOptions(browser_name)
    elif profile in ["visible", "debug"]:
        opts = ProfileTwoDriverOptions(browser_name)

    browser = Browser(browser_name, environment)
    browser.build_browser(opts.get_profile_options())

    yield browser

    if profile in ["clean", "visible"]:
        browser.exit_browser()


@pytest.fixture(scope="session")
def start_session(start_servers):
    yield start_servers


@pytest.fixture(scope="session")
def start_servers(set_options):
    print("Starting Server 1")
    print(f"Running Server Env: {set_options[1]}")
    yield set_options
    print("Closing Server 1")

@pytest.fixture(scope="session")
def set_options(request):
    # We can add handlers for each options here to catch when the user input invalid options
    browser = request.config.getoption("--browser")
    env = request.config.getoption("--env")
    profile = request.config.getoption("--profile")
    yield (browser, env, profile)

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default= "stage", help="Test environment :[stage, prod]")
    parser.addoption("--browser", action="store", default= "chrome", help="Browsers :[chrome, firefox, edge]")
    parser.addoption("--profile", action="store", default= "clean", help="['clean', 'visible', 'debug']")
    # clean - Headless, Exit Browser
    # visible - Visible, Exit Browser
    # debug - Visible, Stay Browser


