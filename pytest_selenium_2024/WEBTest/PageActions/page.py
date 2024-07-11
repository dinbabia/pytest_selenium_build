from PageActions.WebActions import NavigationHandler, InteractionHandler


class Page:

    def __init__(self, driver):
        self.navigation = NavigationHandler(driver)
        self.interaction = InteractionHandler(driver)
