import pytest
from test_base import BaseCase


class TestSettings(BaseCase):
    authorize = True

    # not really a teardown due to inability to actually delete a newly created profile
    @pytest.fixture(autouse=True)
    def setup_settings(self):
        self.register_page = self.landing_page.open_register_page()
        
        self.lk_page = self.register_page.register_advertiser_physical("roflanpotsan@ya.ru", should_redirect=True)
        self.settings_page = self.lk_page.open_general_settings()

        yield

        self.settings_page.delete_lk()
        self.settings_page.wait().until(lambda driver: driver.current_url == self.landing_page.url)

    def test_cancel_changes(self, constants):
        self.settings_page.set_lk_name(constants['name'])
        self.settings_page.cancel_changes()
        assert self.settings_page.get_lk_name() == ''

    def test_save_changes(self, constants):
        
        self.settings_page.set_lk_name(constants['name'])
        self.settings_page.set_lk_tax_payer_id(constants['tpid'])
        self.settings_page.save_changes()
        self.settings_page.reload()

        assert self.settings_page.get_lk_name() == constants['name']
        assert self.settings_page.get_lk_tax_payer_id() == constants['tpid']

    def test_add_email(self, constants):
        self.settings_page.setup_name_and_tpid(name=constants['name'], tpid=constants['tpid'])
        self.settings_page.add_email(constants['email'])
        self.settings_page.save_changes()
        self.settings_page.wait(2)
        self.settings_page.reload()
        assert constants['email'] in self.settings_page.get_email_confirmation_msg()

    def test_request_api_access(self, constants):
        self.settings_page.setup_name_and_tpid(name=constants['name'], tpid=constants['tpid'])
        self.settings_page.request_api_access(phone=constants['phone'])
        assert self.settings_page.get_api_key() != ""

    def test_update_notifications(self):
        assert len(self.settings_page.get_notifications_list()) != 0
        self.settings_page.open_notification_settings_tab()
        self.settings_page.toggle_all_notifications()
        self.settings_page.save_changes()
        self.settings_page.reload()
        self.settings_page.open_notification_settings_tab()
        assert len(self.settings_page.get_notifications_list()) == 0
