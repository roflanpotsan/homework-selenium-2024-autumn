from ui.pages.ads_vk_base import BasePage
from ui.locators.vk_ads_locators_budget import BudgetPageLocators
from selenium.webdriver.support import expected_conditions as EC

class BudgetPage(BasePage):
    locators = BudgetPageLocators

    def open_recharge_modal(self):
        self.click(self.locators.RECHARGE_BUTTON)
        self.wait( timeout=10).until(EC.presence_of_element_located(self.locators.AMOUNT_INPUT))  # Ожидание появления инпутов

    def fill_input(self, locator, value):
        input_field = self.find(locator)
        input_field.clear()
        input_field.send_keys(value)

    def get_input_value(self, locator):
        return self.find(locator).get_attribute("value")

    def wait_for_value(self, locator, expected_value, timeout=15):
        self.wait(timeout).until(
            lambda driver: driver.find_element(*locator).get_attribute("value") == expected_value,
            message=f"Value in {locator} did not change to {expected_value} within timeout"
        )
