import pytest
from ads_vk_test_base import BaseCase
from ui.pages.ads_vk_settings import SettingsPage


class TestRegister(BaseCase):
    authorize = True

    # no teardown due to inability to actually delete a newly created profile
    @pytest.fixture(autouse=True)
    def setup_settings(self):
        self.landing_page.login()
        self.lk_page = self.landing_page.open_profile('last() - 1')
        self.settings_page = self.lk_page.open_general_settings()
        self.settings_page.default_timeout = 10

    def test_notification_tab(self):
        self.settings_page.open_notification_settings_tab()