from core.WebActions import WebActions as WA

class DemoActions(WA):

    def sample_action(self):
        print("Sample Demo Action")
        print(f"URL: {self._url}")
        print(f"Title: {self._title}")
