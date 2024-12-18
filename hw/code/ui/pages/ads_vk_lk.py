from ui.pages.ads_vk_base import BasePage
from ui.pages.ads_vk_settings import SettingsPage
from ui.locators.vk_ads_locators import LKPageLocators

class LKPage(BasePage):

    locators = LKPageLocators
    url = 'https://ads.vk.com/hq/overview'
    default_timeout = 15

    def open_general_settings(self):
        self.click(self.locators.GENERAL_SETTINGS)
        return SettingsPage(self.driver)