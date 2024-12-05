import pytest
from ads_vk_test_base import BaseCase


class TestLogin(BaseCase):
    authorize = True

    def test_login(self):
        self.landing_page.login()
        self.landing_page.open_profile()
        self.landing_page.wait(10).until(lambda driver: driver.current_url == 'https://ads.vk.com/hq/overview')