import pyperclip
from ui.pages.ads_vk_base import BasePage
from ui.locators.vk_ads_locators import SettingsPageLocators


class SettingsPage(BasePage):

    locators = SettingsPageLocators
    url = 'https://ads.vk.com/hq/settings'
    default_timeout = 10

    def get_lk_email(self):
        return self.find(self.locators.LK_EMAIL).get_attribute('value')

    def get_lk_name(self):
        return self.find(self.locators.LK_NAME).get_attribute('value')
    
    def get_lk_tax_payer_id(self):
        return self.find(self.locators.LK_TAX_PAYER_ID).get_attribute('value')
    
    def open_notification_settings_tab(self):
        self.click(self.locators.NOTIFICATION_SETTINGS_TAB)

    def open_access_settings_tab(self):
        self.click(self.locators.ACCESS_SETTINGS_TAB)

    def set_lk_name(self, name=""):
        self.find(self.locators.LK_NAME).clear()
        self.input(self.locators.LK_NAME, name)
    
    def set_lk_tax_payer_id(self, tpid=""):
        self.find(self.locators.LK_TAX_PAYER_ID).clear()
        self.input(self.locators.LK_TAX_PAYER_ID, tpid)

    def save_lk_credentials(self, name=None, tax_payer_id=None, email=None):
        if name:
            self.set_lk_name(name)
        if tax_payer_id:
            self.set_lk_tax_payer_id(tax_payer_id)
        if email:
            self.add_email(email)
        self.save_changes()
    
    def cancel_changes(self):
        self.click(self.locators.CANCEL_CHANGES_BTN)

    def save_changes(self):
        self.click(self.locators.SAVE_CHANGES_BTN)

    def delete_lk(self):
        self.click(self.locators.GENERAL_SETTINGS)
        self.became_invisible(self.locators.DELETE_ACC_BTN, 5)
        self.click(self.locators.DELETE_ACC_BTN)
        self.became_invisible(self.locators.DELETE_ACC_CONFIRM, 5)
        self.click(self.locators.DELETE_ACC_CONFIRM)
        self.became_invisible(self.locators.DELETE_ACC_CONFIRM, 5)

    def add_email(self, email=""):
        self.click(self.locators.ADD_EMAIL_BTN)
        self.input(self.locators.ADD_EMAIL_INPUT, email)

    def get_email_confirmation_msg(self):
        return self.find(self.locators.EMAIL_MSG).text
    
    def request_api_access(self, phone=""):
        self.click(self.locators.REQUEST_API_BTN)
        self.input(self.locators.API_PHONE_INPUT, phone)
        self.click(self.locators.API_SUBMIT_REQ)

    def get_api_key(self):
        self.click(self.locators.API_KEY_BTN)
        return pyperclip.paste()
    
    def toggle_all_notifications(self):
        self.click(self.locators.EMAIL_NOTIFICATIONS_SWITCH)
        self.click(self.locators.VK_NOTIFICATIONS_SWITCH)

    def get_notifications_list(self):
        return self.driver.find_elements(*self.locators.CHECKBOXES)
    
    def get_lk_id(self):
        return self.find(self.locators.LK_ID).text
    
    def switch_to_first_accout(self):
        self.click(self.locators.ACCOUNT_SWITCH_BTN)
        self.became_invisible(self.locators.ACCOUNT_SWITCH_BTN, 1)
        self.click(self.locators.FIRST_ACC)
        self.became_invisible(self.locators.FIRST_ACC, 1)

    def switch_to_current_account(self):
        self.click(self.locators.ACCOUNT_SWITCH_BTN)
        self.became_invisible(self.locators.ACCOUNT_SWITCH_BTN, 1)
        self.click(self.locators.CURRENT_ACC)
        self.became_invisible(self.locators.CURRENT_ACC, 1)

    def create_access(self, lk_id=""):
        self.click(self.locators.ADD_ACCESS)
        self.input(self.locators.ACCESS_ID_INPUT, lk_id)
        self.click(self.locators.ACCESS_SUBMIT_BTN)

    def remove_access(self):
        self.click(self.locators.REMOVE_ACCESS_BTN)
        self.click(self.locators.REMOVE_ACCESS_CONFIRM)
    
    def setup_name_and_tpid(self, name, tpid):
        self.set_lk_name(name)
        self.set_lk_tax_payer_id(tpid)
        self.save_changes()
        self.reload()