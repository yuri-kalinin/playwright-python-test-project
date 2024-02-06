from .elembase import ElemBase, Page

class Link(ElemBase):
    def __init__(self, page: Page, sref: str):
        super().__init__(page.locator(f'[ui-sref="{sref}"]'))