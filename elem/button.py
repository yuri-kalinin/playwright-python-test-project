from .elembase import ElemBase, Page

class Button(ElemBase):
    def __init__(self, page: Page, click: str):
        super().__init__(page.locator(f'[ng-click="{click}"]'))