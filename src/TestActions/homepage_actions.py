from core.WebActions import WebActions as WA
import locators.homepage_resx as _resx_

class LoginActions(WA):


    def fill_up_login_form(self):
       
        # Enter Username
        self._SendKeys(by_locator=_resx_.login_form['username'], text="Din Babia")

        # Enter Password
        self._SendKeys(by_locator=_resx_.login_form['password'], text="123")

        self._Click(by_locator=_resx_.login_button)
        alert_message = self._GetAlertMessage()
        
        assert alert_message == "Error Password or Username", f"{alert_message} != 'Error Password or Username'"
        print(f"\nAlert Message: {alert_message}")
    
    def get_delayed_text(self):

        # Get TextWillBeDisplayedWithDelay
        delayed_text = self._GetElementText(by_locator=_resx_.delayed_text)
        assert delayed_text == "This text is displayed after 10 seconds of wait.", f"{delayed_text} != 'This text is displayed after 10 seconds of wait.'"
        print(f"\nDelayed text: {delayed_text}")

    def get_headers_on_the_table(self):

        # Get headers on the table
        table_headers = self._GetElementsText(by_locator= _resx_.table_headers)
        headers_list = ['Name', 'Age', 'Place']

        print("\n")
        # Assert headers are correct
        for count in range(len(headers_list)):
            print(f"{table_headers[count]} vs {headers_list[count]}")
            assert table_headers[count] == headers_list[count], f"{table_headers[count]} != {headers_list[count]}"

        

