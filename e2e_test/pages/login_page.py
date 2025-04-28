from e2e_test.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    user_name  = (By.ID, 'user-name')
    password  = (By.ID, 'password')
    inventory_list = (By.CLASS_NAME, "inventory_list")
    login_button = (By.ID, "login-button")

    def login(self, user, password):
        self.type_text(self.user_name, user)
        self.type_text(self.password, password)
        self.click(self.login_button)

    def get_item_after_login(self):
        el = self.get_element(self.inventory_list)
        return el

