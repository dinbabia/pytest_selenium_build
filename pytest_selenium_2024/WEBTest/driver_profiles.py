from driver_config import SelectDriverOptions, ChromeDriverOptions, FirefoxDriverOptions


class ProfileDriverOptions:
    def __init__(self, browser_name):
        selected_driver_option = SelectDriverOptions(browser_name)
        if browser_name == "chrome":
            self.driver_options = ChromeDriverOptions(selected_driver_option.opts)
        elif browser_name == "firefox":
            self.driver_options = FirefoxDriverOptions(selected_driver_option.opts)

    def get_profile_options(self):
        return self.driver_options.options


class ProfileOneDriverOptions(ProfileDriverOptions):

    def __init__(self, browser_name):
        super().__init__(browser_name)
        self.driver_options.set_to_headless()

class ProfileTwoDriverOptions(ProfileDriverOptions):
    def __init__(self, browser_name):
        super().__init__(browser_name)
