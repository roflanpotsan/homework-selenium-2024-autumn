from selenium.webdriver.common.by import By

class LandingPageLocators:
    LOGIN_BUTTON = (By.XPATH, '//*[@class="ButtonCabinet_primary__LCfol"]')

    # NOT LANDING PAGE RELATED, BUT THERE'S NO OTHER PLACE FOR THEM
    CONTINUE_BUTTON = (By.XPATH, '//div[@class="vkc__LoginConnectOrPhone__connectButton"]/button[1]')
    def AT_PROFILE_BUTTON(profile_number):
        return (By.XPATH, f'//div[@class="vkc__OrganizationList__listWrapper"]/div[{profile_number}]')
    AT_PROFILE_BTNS = (By.XPATH, '//div[@class="vkc__OrganizationList__listWrapper"]')
    CREATE_PROFILE_BUTTON = (By.XPATH, f'//div[@class="vkc__OrganizationList__listWrapper"]/div[last()]')
    BUDGET_LINK = (By.CSS_SELECTOR, '[data-entityid="budget"]')  # Ссылка на страницу бюджета
    AUDITORY_LINK = (By.CSS_SELECTOR, '[data-entityid="audience"]')


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

    GENERAL_SETTINGS_TAB = (By.CSS_SELECTOR, '[data-testid="tabs-item-settings"]')
    NOTIFICATION_SETTINGS_TAB = (By.CSS_SELECTOR, '[data-testid="tabs-item-settings.notifications"]')
    ACCESS_SETTINGS_TAB = (By.CSS_SELECTOR, '[data-testid="tabs-item-settings.access"]')

    CANCEL_CHANGES_BTN = (By.CSS_SELECTOR, '[data-testid="settings-cancel"]')
    SAVE_CHANGES_BTN = (By.CSS_SELECTOR, '[data-testid="settings-save"]')

    DELETE_ACC_BTN = (By.CSS_SELECTOR, '.DeleteAccount_button__BEy7F')
    DELETE_ACC_CONFIRM = (By.XPATH, '//div[@class="DeleteAccountConfirmModal_actions__kum6t"]//button[2]')

    ADD_EMAIL_BTN = (By.CSS_SELECTOR, '[data-testid="add-email"]')
    ADD_EMAIL_INPUT = (By.XPATH, '//div[@class="Emails_emails__QNEvR"]//div[last()]//input[1]')
    EMAIL_MSG = (By.CSS_SELECTOR, '.Warning_container__WlR61')

    REQUEST_API_BTN = (By.XPATH, '//div[@class="ApiAccess_wrapper__QEwLb"]//div[1]')
    API_PHONE_INPUT = (By.XPATH, '//div[@class="ApiAccessModal_content__U1JWa"]//div[2]//span[1]//input[1]')
    API_SUBMIT_REQ = (By.CSS_SELECTOR, '[data-testid="submit"]')
    API_KEY_BTN = (By.CSS_SELECTOR, '.ApiAccess_copyButton__IaW1-')

    EMAIL_NOTIFICATIONS_SWITCH = (By.XPATH, '//div[@class="vkuiCell Emails_item__x1pUR"]//div[1]')
    VK_NOTIFICATIONS_SWITCH = (By.XPATH, '//div[@class="vkuiCell VkNotificationSwitch_item__ASY5p"]//div[1]')
    CHECKBOXES = (By.CSS_SELECTOR, 'input[type="checkbox"]:checked')

    LK_ID = (By.XPATH, '//div[@class="Account_items__qVbu1"]//span[1]')
    ACCOUNT_SWITCH_BTN = (By.CSS_SELECTOR, '.AccountSwitch_changeAccountButton__o5T9V')
    FIRST_ACC = (By.XPATH, '//div[@class="AccountSwitch_accounts__4A6vj"]//div[2]//div[1]')
    CURRENT_ACC = (By.XPATH, '//div[@class="AccountSwitch_accounts__4A6vj"]//div[last()]//div[1]')

    ADD_ACCESS = (By.CSS_SELECTOR, '[data-testid="add-user"]')
    ACCESS_ID_INPUT = (By.XPATH, '//div[@class="Add_form__0z6FU"]//div[1]//span[1]//input[1]')
    ACCESS_SUBMIT_BTN = (By.CSS_SELECTOR, '[data-testid="submit"]')

    REMOVE_ACCESS_BTN = (By.CSS_SELECTOR, '[data-test="remove-button"]')
    REMOVE_ACCESS_CONFIRM = (By.XPATH, '//div[@class="Remove_buttons__hSad4"]//button[2]')