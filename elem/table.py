from .elembase import ElemBase, Page

class Table(ElemBase):
    def __init__(self, page: Page, repeat: str):
        super().__init__(page.locator(f'[ng-repeat="{repeat}"]'))
    
    def get_data(self) -> list[list[str]]:
        return [row.locator('td').all_inner_texts() for row in self.locator.all()]
    
    def wait_until_contains(self, value: str, timeout: float=2_000):
        try:
            self.locator.get_by_text(value).wait_for(timeout=timeout)
        except:
            pass