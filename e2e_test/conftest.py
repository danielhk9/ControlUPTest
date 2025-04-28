import pytest
from selenium import webdriver

from e2e_test.config import USERNAME, PASSWORD, BASE_URL
from e2e_test.pages.inventory_page import InventoryPage
from e2e_test.pages.login_page import LoginPage


@pytest.fixture(scope="session")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {
        "profile.password_manager_leak_detection": False
        })
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def login(driver):
    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)
    inventory_list_el = login_page.get_item_after_login()
    assert inventory_list_el, "Login failed!"


@pytest.fixture
def inventory_setup(driver):
    inventory_page = InventoryPage(driver)
    yield inventory_page



