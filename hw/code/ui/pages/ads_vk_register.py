import time
from ui.pages.ads_vk_base import BasePage
from ui.locators.vk_ads_locators import RegisterPageLocators

class RegisterPage(BasePage):

    locators = RegisterPageLocators
    url = 'https://ads.vk.com/hq/registration'
    
    def register_advertiser_physical(self, email, tax_payer_idx="", name=""):
        self.click(self.locators.CREATE_PROFILE_CARD)
        self.click(self.locators.LK_ADVERTISER)
        self.click(self.locators.LK_PHYS)
        self.input(self.locators.EMAIL, email)
        self.input(self.locators.TAX_PAYER_INDEX, tax_payer_idx)
        self.input(self.locators.NAME, name)
        self.click(self.locators.SUBMIT)
        # time.sleep(5)
    
    def register_advertiser_company(self, email):
        self.click(self.locators.CREATE_PROFILE_CARD)
        self.click(self.locators.LK_ADVERTISER)
        self.click(self.locators.LK_COMPANY)
        self.input(self.locators.EMAIL, email)
        self.click(self.locators.SUBMIT)
        # time.sleep(5)
        
    def register_agency(self, email):
        self.click(self.locators.CREATE_PROFILE_CARD)
        self.click(self.locators.LK_AGENCY)
        self.click(self.locators.LK_COMPANY)
        self.input(self.locators.EMAIL, email)
        self.click(self.locators.SUBMIT)
        # time.sleep(5)

    def get_email_error_msg(self):
        return self.find(self.locators.EMAIL_ERROR_MSG)