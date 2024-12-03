import pytest
from ads_vk_test_base import BaseCase


class TestLanding(BaseCase):
    authorize = False
    def test_landing_load(self):
        assert self.driver.current_url == self.landing_page.url