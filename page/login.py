import elem
from .pagebase import PageBase

class Login(PageBase):

    def __init__(self, url, page):
        super().__init__(url, page)
        self.url = url + "/#!/login"
        self.username = elem.Text(page, model="credentials.username")
        self.password = elem.Text(page, model="credentials.password")
        self.accept_terms_and_conditions = elem.Checkbox(page, model="credentials.accept_terms_and_conditions")
        self.login_button = elem.Button(page, click="submitAction()")

    def open(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.username.set_value(username)
        self.password.set_value(password)
        self.accept_terms_and_conditions.click()
        self.login_button.click()
