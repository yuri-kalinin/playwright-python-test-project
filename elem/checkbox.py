from .elembase import ElemBase, Page

class Checkbox(ElemBase):
    def __init__(self, page: Page, model: str):
        super().__init__(page.locator(f'[ng-model="{model}"]'))

    def set_value(self, value: bool):
        if self.locator.is_checked() != value:
            self.locator.locator("xpath=..").click()

    def get_value(self):
        return self.locator.is_checked()