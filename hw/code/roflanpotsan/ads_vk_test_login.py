import pytest
from ads_vk_test_base import BaseCase


class TestLogin(BaseCase):
    authorize = False


    @pytest.mark.usefixtures('credentials')
    def test_login(self, credentials):
        self.landing_page.login(credentials['EMAIL'], credentials['PASSWORD'])
        assert self.driver.current_url == 'https://education.vk.company/feed/'