from selenium.webdriver.common.by import By

class LandingPageLocators:
    LOGIN_BUTTON = (By.XPATH, '//*[@class="ButtonCabinet_primary__LCfol"]')

    # NOT LANDING PAGE RELATED, BUT THERE'S NO OTHER PLACE FOR THEM
    CONTINUE_BUTTON = (By.XPATH, '//div[@class="vkc__LoginConnectOrPhone__connectButton"]/button[1]')
    def AT_PROFILE_BUTTON(profile_number):
        return (By.XPATH, f'//div[@class="vkc__OrganizationList__listWrapper"]/div[{profile_number}]')
    CREATE_PROFILE_BUTTON = (By.XPATH, f'//div[@class="vkc__OrganizationList__listWrapper"]/div[last()]')
    BUDGET_LINK = (By.CSS_SELECTOR, '[data-entityid="budget"]')  # Ссылка на страницу бюджета


class RegisterPageLocators:
    CREATE_PROFILE_CARD = (By.XPATH, '//*[@class="CardButton_cardButton__rNuEi"]')
    LK_ADVERTISER = (By.XPATH, '//*[@class="registration_panelInnerWrapperContentForm__x3heD"]/div[1]/label[1]')
    LK_AGENCY = (By.XPATH, '//*[@class="registration_panelInnerWrapperContentForm__x3heD"]/div[1]/label[2]')
    LK_PHYS = (By.XPATH, '//*[@class="registration_panelInnerWrapperContentForm__x3heD"]/div[5]/label[1]')
    LK_COMPANY = (By.XPATH, '//*[@class="registration_panelInnerWrapperContentForm__x3heD"]/div[5]/label[2]')

    EMAIL = LOGIN_BUTTON = (By.XPATH, '//input[@name="email"]')
    TAX_PAYER_INDEX = (By.XPATH, '//input[@name="inn"]')
    NAME = (By.XPATH, '//input[@name="name"]')
    SUBMIT = (By.XPATH, '//button[@type="submit"]')

    EMAIL_ERROR_MSG = (By.XPATH, '//*[@class="registration_panelInnerWrapperContentForm__x3heD"]/div[4]/span[2]')
    TAX_PAYER_INDEX_ERROR_MSG = (By.XPATH, '//*[@class="registration_panelInnerWrapperContentForm__x3heD"]/div[6]/span[2]')
    NAME_ERROR_MSG = (By.XPATH, '//*[@class="registration_panelInnerWrapperContentForm__x3heD"]/div[7]/span[2]')

    LANG_TOGGLE_EN = (By.XPATH, '//*[@class="vkuiSegmentedControl__in"]//label[2]')
    LANG_TOGGLE_RU = (By.XPATH, '//*[@class="vkuiSegmentedControl__in"]//label[1]')

class LKPageLocators:
    GENERAL_SETTINGS = (By.XPATH, '//a[@data-route="settings"]')

class SettingsPageLocators:
    GENERAL_SETTINGS = (By.XPATH, '//a[@data-route="settings"]')
    LK_EMAIL = (By.XPATH, '//input[@data-testid="general-email"]')
    LK_NAME = (By.XPATH, '//input[@data-testid="general-ord-name"]')
    LK_TAX_PAYER_ID = (By.XPATH, '//input[@data-testid="general-ord-inn"]')

    GENERAL_SETTINGS_TAB = (By.XPATH, '//div[@class="vkuiTabs__in"]//div[1]')
    NOTIFICATION_SETTINGS_TAB = (By.XPATH, '//div[@class="vkuiTabs__in"]//div[3]')
    ACCESS_SETTINGS_TAB = (By.XPATH, '//div[@class="vkuiTabs__in"]//div[3]')