from ui.pages.ads_vk_base import BasePage
from ui.pages.ads_vk_auth import MainPage
from ui.locators.vk_ads_locators import LandingPageLocators

class LandingPage(BasePage):

    locators = LandingPageLocators
    url = 'https://ads.vk.com/'
