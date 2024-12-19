from ui.pages.ads_vk_base import BasePage
from ui.locators.vk_ads_locators import RegisterPageLocators
from ui.pages.ads_vk_lk import LKPage

class RegisterPage(BasePage):

    locators = RegisterPageLocators
    url = 'https://ads.vk.com/hq/registration'
    default_timeout = 15
    
    def register_advertiser_physical(self, email="", tax_payer_idx="", name="", should_redirect=False):
        self.click(self.locators.CREATE_PROFILE_CARD)
        self.click(self.locators.LK_ADVERTISER)
        self.click(self.locators.LK_PHYS)
        self.input(self.locators.EMAIL, email)
        self.input(self.locators.TAX_PAYER_INDEX, tax_payer_idx)
        self.input(self.locators.NAME, name)
        self.click(self.locators.SUBMIT)
        if should_redirect:
            return LKPage(self.driver)
        
    def set_lang_en(self):
        print(self.find(self.locators.LANG_TOGGLE_EN))
        self.click(self.locators.LANG_TOGGLE_EN)
    
    def set_lang_ru(self):
        self.click(self.locators.LANG_TOGGLE_RU)

    def get_email_error_msg(self):
        return self.find(self.locators.EMAIL_ERROR_MSG).text
    
    def get_tax_payer_index_error_msg(self):
        return self.find(self.locators.TAX_PAYER_INDEX_ERROR_MSG).text
    
    def get_name_error_msg(self):
        return self.find(self.locators.NAME_ERROR_MSG).text
    
    def get_create_account_button_text(self):
        return self.find(self.locators.CREATE_PROFILE_CARD).text