from selenium.webdriver.common.by import By

from e2e_test.pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    REMOVE_FROM_CART = (By.XPATH,  '//button[text()="Remove"]')

    def get_inventory_items(self):
        return self.get_elements(self.INVENTORY_ITEM)

    def add_inventory_item_to_cart_by_index(self, item):
        add_button = self.find_element_inside(item, self.ADD_TO_CART_BUTTON)
        self.click(element=add_button)

    def get_cart_item(self):
        return self.get_element(self.CART_BADGE)


    def remove_item_from_cart(self, item):
        remove_button = self.find_element_inside(item, self.REMOVE_FROM_CART)
        self.click(element=remove_button)