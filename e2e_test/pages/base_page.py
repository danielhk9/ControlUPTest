from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=2):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False

    def wait_for_elements(self, locator):
        try:
            return self.wait.until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            assert False, f"Elements {locator} were not visible after {self.wait._timeout} seconds."

    def get_element(self, locator):
        return self.wait_for_element(locator)

    def get_elements(self, locator):
        return self.wait_for_elements(locator)

    def click(self, locator=True, element=None):
        if element:
            element.click()
        else:
            self.get_element(locator).click()

    def type_text(self, locator, text):
        element = self.get_element(locator)
        element.clear()
        element.send_keys(text)

    def is_displayed(self, locator):
        try:
            return self.get_element(locator).is_displayed()
        except TimeoutException:
            return False

    def find_element_inside(self, parent_element, locator):
        return parent_element.find_element(*locator)


