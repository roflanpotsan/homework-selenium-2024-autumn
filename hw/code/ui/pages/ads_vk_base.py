import time

import allure
from selenium.webdriver.remote.webelement import WebElement
from ui.locators import vk_ads_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):

    locators = vk_ads_locators.LandingPageLocators()
    url = 'https://ads.vk.com/'
    default_timeout = 5

    def is_opened(self, timeout=default_timeout):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedExeption(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def wait(self, timeout=default_timeout):
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=default_timeout):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Click')
    def click(self, locator, timeout=default_timeout) -> WebElement:
        try:
            elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
            elem.click()
        except:
            pass

    @allure.step('Input')
    def input(self, locator, data, timeout=default_timeout):
        elem = self.find(locator, timeout=timeout)
        elem.send_keys(data)