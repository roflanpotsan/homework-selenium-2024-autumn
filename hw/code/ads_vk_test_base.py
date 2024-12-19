from contextlib import contextmanager

import pytest

from ui.pages.ads_vk_landing import LandingPage
from ui.pages.ads_vk_register import RegisterPage
from ui.pages.ads_vk_budget import BudgetPage
from ui.pages.ads_vk_auditory import AuditoryPage
from ui.pages.ads_vk_commersion import CommersionPage

class BaseCase:
    authorize = True

    @contextmanager
    def switch_to_window(self, current, close=False):
        for w in self.driver.window_handles:
            if w != current:
                self.driver.switch_to.window(w)
                break
        yield
        if close:
            self.driver.close()
        self.driver.switch_to.window(current)

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, credentials):
        self.driver = driver
        self.config = config

        self.landing_page = LandingPage(driver)
        self.budget_page = BudgetPage(driver)
        self.auditory_page = AuditoryPage(driver)
        self.commersion_page = CommersionPage(driver)
        if self.authorize:
            cookies = credentials.get('COOKIES', [])
        
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        
            # Refresh page to apply cookies
            self.driver.refresh()

            self.main_page = self.landing_page.login()