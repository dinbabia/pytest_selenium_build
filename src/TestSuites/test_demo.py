from conftest import DriverInfo
from test_base import BaseTest
from TestActions.demo_actions import DemoActions
from TestActions.homepage_actions import LoginActions


class Test_Demo(BaseTest):

    def login_success(self):
        login_action = LoginActions(self.driver)
        print("Loggin IN")
        login_action.fill_up_login_form()
    
    def setup_connection(self):
        print("Setting up VPN connection")

    def test_demo_run(self):
        # Setting up VPN or Database if needed
        self.setup_connection()

        # Step 1: Check URL and Title of the page
        action = DemoActions(self.driver)
        action.sample_action()
        
        # Step 1: Login
        self.login_success()

        
        

    

  