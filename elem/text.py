from .elembase import ElemBase, Page

class Text(ElemBase):
    def __init__(self, page: Page, model: str):
        super().__init__(page.locator(f'[ng-model="{model}"]'))

    def set_value(self, value):
        self.locator.clear()
        self.locator.fill(value)

    def get_value(self):
        return self.locator.input_value()