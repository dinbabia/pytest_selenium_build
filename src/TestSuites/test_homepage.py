from conftest import DriverInfo
from test_base import BaseTest
from TestActions.demo_actions import DemoActions
from TestActions.homepage_actions import LoginActions


class Test_Homepage(BaseTest):



    def test_login_credentials(self):
    
        action = LoginActions(self.driver)
        action.fill_up_login_form()
    
    def test_text_delay(self):
    
        action = LoginActions(self.driver)
        action.get_delayed_text()

    def test_table_headers(self):
    
        action = LoginActions(self.driver)
        action.get_headers_on_the_table()
     
        