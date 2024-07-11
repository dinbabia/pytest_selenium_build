from ApiTest import api_requests
from PageActions.LoginPage import LoginPageActions

def test_sample(browser):
    print(f"Cat Random: {api_requests.get_random_cat()}")

    login_page = LoginPageActions(browser.driver)
    login_page.go_to_facebook_page()
    login_page.enter_email("yeheeey")
    login_page.enter_password("123123")
    login_page.click_login_button()
    print("Test Run")
