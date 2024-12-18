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

    # def delete_lk(self):
    #     self.click(self.locators.GENERAL_SETTINGS)
    #     self.click(self.locators.DELETE_LK)
    #     self.click(self.locators.DELETE_LK_CONFIRM)