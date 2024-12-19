from test_base import BaseCase
class TestBudget(BaseCase):
    authorize = True  # Предполагается, что авторизация уже настроена в BaseCase

    def navigate_to_budget(self):
        self.landing_page.login()
        self.landing_page.open_profile()
        self.landing_page.wait(15).until(lambda driver: driver.current_url == 'https://ads.vk.com/hq/overview')
        self.budget_page.click(self.landing_page.locators.BUDGET_LINK)
        # self.budget_page.find(self.budget_page.locators.RECHARGE_BUTTON, timeout=10)

    def test_amount_to_vat_conversion(self):
        self.navigate_to_budget()
        self.budget_page.open_recharge_modal()

        self.budget_page.fill_input(self.budget_page.locators.AMOUNT_INPUT, "600")
        # self.budget_page.wait_for_value(self.budget_page.locators.AMOUNT_WITHOUT_VAT_INPUT, "500")
        assert self.budget_page.get_input_value(self.budget_page.locators.AMOUNT_WITHOUT_VAT_INPUT) == "500 ₽", \
            "Conversion from amount to amountWithoutVat failed"

    def test_vat_to_amount_conversion(self):
        self.navigate_to_budget()
        self.budget_page.open_recharge_modal()

        self.budget_page.fill_input(self.budget_page.locators.AMOUNT_WITHOUT_VAT_INPUT, "500")
        # self.budget_page.wait_for_value(self.budget_page.locators.AMOUNT_INPUT, "600")
        assert self.budget_page.get_input_value(self.budget_page.locators.AMOUNT_INPUT) == "600 ₽", \
            "Conversion from amountWithoutVat to amount failed"
