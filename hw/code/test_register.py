import pytest
from test_base import BaseCase

class TestRegister(BaseCase):
    authorize = True

    # no teardown due to inability to actually delete a newly created profile
    @pytest.fixture(autouse=True)
    def setup_register(self):
        self.register_page = self.landing_page.open_register_page()

    def test_register_correct_inputs(self, constants):
        input_email = constants['base_email']
        input_name = constants['name']
        input_tax_payer_id = constants['tpid']
        self.lk_page = self.register_page.register_advertiser_physical(email=input_email, 
                                                                             name=input_name, 
                                                                             tax_payer_idx=input_tax_payer_id,
                                                                             should_redirect=True)
        self.settings_page = self.lk_page.open_general_settings()
        assert self.settings_page.get_lk_name() == input_name
        assert self.settings_page.get_lk_tax_payer_id() == input_tax_payer_id
        assert self.settings_page.get_lk_email() == input_email

        self.settings_page.delete_lk()
        self.settings_page.wait().until(lambda driver: driver.current_url == self.landing_page.url)

    def test_register_incorrect_email(self, constants):
        input_email = constants['incorrect_email']
        self.register_page.register_advertiser_physical(email=input_email)
        assert self.register_page.get_email_error_msg() == 'Некорректный email адрес'
    
    def test_register_empty_email(self):
        self.register_page.register_advertiser_physical()
        assert self.register_page.get_email_error_msg() == 'Обязательное поле'
    
    def test_register_incorrect_tax_payer_index(self, constants):
        input_email = constants['base_email']
        input_tax_payer_id = constants['incorrect_tpid']
        self.lk_page = self.register_page.register_advertiser_physical(email=input_email, 
                                                                             name="", 
                                                                             tax_payer_idx=input_tax_payer_id)
        assert self.register_page.get_tax_payer_index_error_msg() == 'Некорректный ИНН'

    def test_register_incorrect_name(self, constants):
        input_email = constants['base_email']
        input_name = constants['incorrect_name']
        input_tax_payer_id = constants['tpid']
        self.lk_page = self.register_page.register_advertiser_physical(email=input_email, 
                                                                             name=input_name, 
                                                                             tax_payer_idx=input_tax_payer_id)
        assert self.register_page.get_name_error_msg() == 'Некорректные символы. Разрешена только кириллица дефис и пробел'

    def test_lang_toggle_ru(self):
        self.register_page.set_lang_ru()
        assert self.register_page.get_create_account_button_text() == 'Создать новый кабинет'

    def test_lang_toggle_en(self):
        self.register_page.set_lang_en()
        assert self.register_page.get_create_account_button_text() == 'Create a new account'

    