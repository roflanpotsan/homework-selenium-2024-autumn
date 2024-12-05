import pytest
from ads_vk_test_base import BaseCase
from ui.pages.ads_vk_register import RegisterPage


class TestRegister(BaseCase):
    authorize = True

    @pytest.fixture(autouse=True)
    def setup_register(self):
        self.landing_page.login()
        self.landing_page.create_profile()
        self.register_page = RegisterPage(self.driver)

    # def test_register_correct_email(self):
    #     self.register_page.register(lk_type=self.register_page.locators.LK_ADVERTISER, 
    #                                 email="roflanpotsan@ya.ru")
    #     self.register_page.wait(10).until(lambda driver: driver.current_url == 'https://ads.vk.com/hq/overview')
        
    
    def test_register_empty_email(self):
        self.register_page.register_advertiser_company(email="")
        
        assert self.register_page.get_email_error_msg().text == 'Обязательное поле'

    def test_register_incorrect_email(self):
        self.register_page.register_advertiser_company(email="hehehe...")
        
        assert self.register_page.get_email_error_msg().text == 'Некорректный email адрес'

    # def test_register_advertiser_company(self):
    #     self.register_page.register_advertiser_company(email="roflanpotsan@ya.ru")
        
    #     self.register_page.wait(10).until(lambda driver: driver.current_url == 'https://ads.vk.com/hq/overview')

    # def test_register_agency(self):
    #     self.register_page.register_agency(email="roflanpotsan@ya.ru")
        
    #     self.register_page.wait(10).until(lambda driver: driver.current_url == 'https://ads.vk.com/hq/overview')