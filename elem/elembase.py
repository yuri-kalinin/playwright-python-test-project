from playwright.sync_api import Locator, Page

class ElemBase(object):

    def __init__(self, locator: Locator):
        self.locator = locator

    def click(self):
        self.locator.click()

    def is_displayed(self):
        return self.locator.is_visible()
    
    def wait_until_displayed(self, visible: bool=True):
        self.locator.wait_for(state="visible" if visible else "hidden")