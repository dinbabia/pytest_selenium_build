from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""
https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html#selenium.webdriver.support.expected_conditions.alert_is_present
EC docu = https://selenium-python.readthedocs.io/waits.html
https://stackoverflow.com/questions/34562061/webdriver-click-vs-javascript-click
https://stackoverflow.com/questions/59130200/selenium-wait-until-element-is-present-visible-and-interactable
https://www.browserstack.com/guide/selenium-wait-for-page-to-load
"""


class WebActions:

    def __init__(self, driver) -> None:
        self.driver = driver
        self._title = driver.title
        self._url = driver.current_url

        self._explicit_wait = 15
        self._wait = WebDriverWait(self.driver, self._explicit_wait)
     

    def _Click(self, by_locator : tuple):
        '''Web Interaction: Basic left click on a web element (protected)
        
            --------------------------------
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @return : None
        '''
        try:
            self._wait.until(EC.element_to_be_clickable(by_locator)).click()
        except:
            raise Exception (f"Element is not clickable: {by_locator}")


    def _GetElementAttribute(self, by_locator: tuple , attr: str = "value"):
        '''Web Interaction: Get the value attribute of a web element
            --------------------------------
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @param: attr -> Default is value. You can change it other attributes. e.g.[data-value]
        * @return: Attribute value of a web element
        '''
        try:
            element = self._wait.until(EC.visibility_of_element_located(by_locator))
            return element.get_attribute(attr)
        except:
            raise Exception (f"Element is not visible: {by_locator}")


    def _GetElementText(self, by_locator: tuple)->str:
        '''Web Interaction: Get the string/text of a web element
            --------------------------------
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @return: String/Text of a web element
        '''
        try:
            element = self._wait.until(EC.visibility_of_element_located(by_locator))
            return element.text.strip()
        except:
            raise Exception (f"Element is not visible: {by_locator}")


    def _GetElementsText(self, by_locator: tuple)->list:
        try:
            texts = []
            elements = self._wait.until(EC.presence_of_all_elements_located(by_locator))
            for element in elements:
                texts.append(element.text.strip())
            return texts
        except:
            raise Exception (f"Element is not visible: {by_locator}")


    def _SendKeys(self, by_locator : tuple, text: str, clear_field = True):
        '''Web Interaction: Send a string to a web element
            --------------------------------
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @param: text -> The string to be inputted in the element
        * @clear_field -> If you want the input element to be cleared before typing. Default is True.
        * @return: None
        ''' 
        try:
            element = self._wait.until(EC.visibility_of_element_located(by_locator))
            self._wait.until(EC.element_to_be_clickable(by_locator)).click()
            if clear_field:
                element.clear()
            element.send_keys(text)
        except:
            raise Exception (f"Element is not visible: {by_locator}")


    def _GetAlertMessage(self)->str:
        try:
            alert = self._wait.until(EC.alert_is_present())
            return alert.text.strip()
        except:
            raise Exception (f"Alert is not present")


    def web_wait(self, by_locator):
        '''Web Interaction: Wait for a certain element 
            --------------------------------
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @return: None
        '''
        self._wait.until(EC.presence_of_element_located(by_locator))
        self._wait.until(EC.visibility_of_element_located(by_locator))
    
        