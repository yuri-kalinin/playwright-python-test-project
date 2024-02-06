from playwright.sync_api import Page
import elem

class PageBase:

    def __init__(self, url: str, page: Page):
        self.url: str = url
        self.page: Page = page

        self.logout = elem.Button(page, click="logout()")
        self.alerts = elem.Link(page, sref="app.alert")

    def wait_loading_complete(self):
        try:
            self.page.locator(".preloader.ng-scope").wait_for(state="visible", timeout=2_000)
        except:
            pass
        self.page.locator("preloader.ng-scope.ng-hide").wait_for(state="hidden")
        self.page.wait_for_function("angular.element(document.body).injector().get('$http').pendingRequests.length === 0")

    def wait_errors(self) -> list[str]:
        return self.page.locator(".message.ng-binding").all_inner_texts()

    def open(self):
        self.page.goto(self.url)
        
    def is_opened(self):
        return self.page.url == self.url