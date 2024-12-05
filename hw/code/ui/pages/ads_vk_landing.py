import time
from ui.pages.ads_vk_base import BasePage
from ui.locators.vk_ads_locators import LandingPageLocators
from ui.pages.ads_vk_register import RegisterPage

class LandingPage(BasePage):

    locators = LandingPageLocators
    url = 'https://ads.vk.com/'

    def login(self):
        self.click(self.locators.LOGIN_BUTTON)
        self.click(self.locators.CONTINUE_BUTTON)

    def open_profile(self, profile_number=1):
       self.click(self.locators.AT_PROFILE_BUTTON(profile_number))

    def create_profile(self):
        self.click(self.locators.CREATE_PROFILE_BUTTON)
        return RegisterPage(self.driver)

