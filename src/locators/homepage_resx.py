from selenium.webdriver.common.by import By

"""
These are the attributes available for By class:
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
"""


delayed_text = (By.ID, "delayedText")


text_area_field = (By.ID, "ta1")
'''text area field in the homepage'''

username = (By.NAME, "userid")
'''Username field'''

password = (By.NAME, "pswrd")
'''Password field'''

login_button = (By.XPATH, "//form[@name='login']/input[3]")

login_form = {
    "username" : (By.NAME, "userid"),
    "password" : (By.NAME, "pswrd"),
}

table_headers = (By.XPATH, "//table[@id='table1']/thead/tr/th")










