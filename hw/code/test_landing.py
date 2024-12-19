from test_base import BaseCase


class TestLanding(BaseCase):
    authorize = False

    def test_landing_load(self):
        assert self.driver.current_url == self.landing_page.url

    def test_vkid_redirect(self):
        self.landing_page.open_vkid_page()
        assert self.driver.current_url.startswith('https://id.vk.com')