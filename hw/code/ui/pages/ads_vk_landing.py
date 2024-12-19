from ui.pages.ads_vk_base import BasePage
from ui.locators.vk_ads_locators import LandingPageLocators
from ui.pages.ads_vk_register import RegisterPage
from ui.pages.ads_vk_lk import LKPage

class LandingPage(BasePage):

    locators = LandingPageLocators
    url = 'https://ads.vk.com/'
    default_timeout = 15

    def open_vkid_page(self):
        self.click(self.locators.LOGIN_BUTTON)

    def login(self):
        self.click(self.locators.LOGIN_BUTTON)
        self.click(self.locators.CONTINUE_BUTTON)

    def open_profile(self, profile_number=1):
        self.click(self.locators.AT_PROFILE_BUTTON(profile_number))
        return LKPage(self.driver)
    
    def open_profile_register(self, profile_number=1):
        self.click(self.locators.AT_PROFILE_BUTTON(profile_number))
        return RegisterPage(self.driver)

    def create_account_profile_exists(self, profile_number='last()-1'):
        return self.open_profile_register(profile_number=profile_number)
    
    def create_account_new_profile(self):
        self.click(self.locators.CREATE_PROFILE_BUTTON)
        return RegisterPage(self.driver)
    
    def reopen(self):
        self.driver.get(self.url)

    def open_register_page(self):
        def open_default(self):
            self.login()
            return self.create_account_profile_exists()
        def open_fallback(self):
            self.login()
            return self.create_account_new_profile()
        return self.retry_operation(operation=lambda: open_default(self), fallback=lambda: open_fallback(self))
