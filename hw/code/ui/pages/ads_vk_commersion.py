from ui.locators.vk_ads_locators_commersion import CommersionPageLocators
from ui.pages.ads_vk_base import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CommersionPage(BasePage):
    locators = CommersionPageLocators

    def click_dismiss_modal_button(self):

        dismiss_modal_button = self.find(self.locators.MODAL_DISMISS_BUTTON, timeout=5)
        dismiss_modal_button.click()

    def click_create_catalog_button(self):
        create_catalog_button = self.wait(timeout=5).until(
            EC.element_to_be_clickable(self.locators.CREATE_CATALOG_BUTTON)
        )
        create_catalog_button.click()

    def fill_input(self, locator, value):
        input_field = self.find(locator)
        input_field.clear()
        input_field.send_keys(value)

    def click_feed_button(self):    
        feed_button = self.find(self.locators.FEED_BUTTON, timeout=5)
        feed_button.click()

    def click_create_button(self):
        self.became_invisible(self.locators.PASSWORD_BUTTON, 2)
        try:
            self.click(self.locators.CREATE_BUTTON, timeout=5)
        except Exception as e:
            print(f"Error occured while clicking create button: {e}")

    def check_catalog_created(self):
        try:
            self.find(self.locators.CATALOG_WINDOW, timeout=10)
        except Exception as e:
            print(f"Error occurred while checking diagnostics all good: {e}")

    def wait_for_window_to_dissapear(self):
        self.became_invisible(self.locators.CREATE_CATALOG_WINDOW, 2)

    def click_catalog_button(self):
        catalog_button = self.find(self.locators.CATALOG_BUTTON, timeout=5)
        catalog_button.click()

    def click_catalog_goods_tab(self):
        catalog_goods_tab = self.find(self.locators.CATALOG_TAB_GOODS, timeout=5)
        catalog_goods_tab.click()

    def click_catalog_goods_tab_settings(self):
        catalog_goods_tab_settings = self.find(self.locators.CATALOG_TAB_GOODS_SETTINGS, timeout=5)
        catalog_goods_tab_settings.click()

    def click_catalog_goods_tab_checkbox(self):
        catalog_goods_tab_checkbox = self.find(self.locators.CATALOG_TAB_GOODS_SETTINGS_CHECKBOX, timeout=5)
        catalog_goods_tab_checkbox.click()

    def click_catalog_goods_tab_confirm(self):
        catalog_goods_tab_confirm = self.wait(timeout=10).until(
            EC.element_to_be_clickable(self.locators.CATALOG_TAB_GOODS_SETTINGS_CONFIRM)
        )
        catalog_goods_tab_confirm.click()

    def click_catalog_groups_tab(self):
        catalog_groups_tab = self.find(self.locators.CATALOG_TAB_GROUPS, timeout=5)
        catalog_groups_tab.click()

    def click_catalog_groups_tab_create(self):
        catalog_groups_tab_create = self.find(self.locators.CATALOG_TAB_GROUPS_CREATE, timeout=5)
        catalog_groups_tab_create.click()

    def click_catalog_groups_tab_filters(self):
        catalog_groups_tab_filters = self.find(self.locators.CATALOG_TAB_GROUPS_CREATE_BY_FILTERS, timeout=5)   
        catalog_groups_tab_filters.click()

    def click_catalog_groups_tab_filters_confirm(self):
        catalog_groups_tab_filters_confirm = self.find(self.locators.CATALOG_GROUPS_CREATE_BY_FILTERS_CONFIRM, timeout=5)
        catalog_groups_tab_filters_confirm.click()

    def click_catalog_diagnostics_tab(self):
        self.became_invisible(self.locators.CATALOG_TAB_GROUPS_CREATE_BY_FILTER_MODAL, 10)
        catalog_diagnostics_tab = self.find(self.locators.CATALOG_TAB_DIAGNOSTICS, timeout=5)
        catalog_diagnostics_tab.click()

    def check_catalog_diagnostics_tab(self):
        try:
            self.find(self.locators.CATALOG_TAB_DIAGNOSTICS_ALL_GOOD, timeout=10)
        except Exception as e:
            print(f"Error occurred while checking diagnostics all good: {e}")

    def click_catalog_settings_button(self):
        catalog_setting_button = self.find(self.locators.CATALOG_SETTINGS_BUTTON, timeout=5)
        catalog_setting_button.click()

    def click_catalog_delete_button(self):
        catalog_delete_button = self.wait(timeout=5).until(
            EC.element_to_be_clickable(self.locators.CATALOG_DELETE_BUTTON)
        )
        catalog_delete_button.click()

    def confirm_delete(self):
        confirm_button = self.wait(timeout=5).until(
            EC.element_to_be_clickable(self.locators.DELETE_BUTTON)
        )
        confirm_button.click()

    def check_catalog_deleted(self):
        self.became_invisible(self.locators.CATALOGS_TABLE, 2)