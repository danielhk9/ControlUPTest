

from e2e_test.pages.inventory_page import InventoryPage
from e2e_test.test_data import EXPECTED_NUMBER_OF_INVENTORY_ITEMS, EXPECTED_CART_COUNT_AFTER_ADDING_ONE_ITEM


def test_get_inventory_number_of_items(driver, login, inventory_setup):
    inventory = inventory_setup.get_inventory_items()
    assert len(inventory) == EXPECTED_NUMBER_OF_INVENTORY_ITEMS, f"Expected 6 inventory items, but git number {len(inventory)}."

def test_add_item_to_cart(driver, login, inventory_setup):
    inventory_item = inventory_setup.add_inventory_item_to_cart_by_index(0)
    cart_badge = inventory_setup.get_cart_item()
    assert cart_badge.text == EXPECTED_CART_COUNT_AFTER_ADDING_ONE_ITEM, f"Cart badge should show '1' instead of {cart_badge.text}, after adding one item to cart."
    inventory_setup.remove_item_from_cart(inventory_item)
