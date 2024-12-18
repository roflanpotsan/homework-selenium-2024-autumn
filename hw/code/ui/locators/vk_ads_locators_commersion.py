from selenium.webdriver.common.by import By


class CommersionPageLocators:
    CREATE_CATALOG_BUTTON = (
        By.XPATH,
        '//button[contains(@class, "vkuiButton") and contains(@class, "vkuiButton--mode-primary")]',
    )
    NAME_INPUT = (By.CSS_SELECTOR, '[data-testid="catalogName-input"]')
    FEED_BUTTON = (By.CSS_SELECTOR, '[data-entityid="url"]')
    FEED_INPUT = (By.CSS_SELECTOR, '[data-testid="catalogUrl-input"]')
    CREATE_BUTTON = (By.CSS_SELECTOR, '[data-testid="submit"]')
    PASSWORD_BUTTON = (
        By.XPATH,
        '//div[contains(@class, "vkuiSimpleCell")]',
    )
    CREATE_CATALOG_WINDOW = (
        By.XPATH,
        '//div[contains(@class, "ModalRoot_componentWrapper__uzHTL")]',
    )
    CATALOG_SETTINGS_BUTTON = (
        By.XPATH,
        '//button[contains(@class, "vkuiButton--mode-outline")]',
    )
    CATALOG_DELETE_BUTTON = (
        By.XPATH,
        '//button[contains(@class, "ModalFooterSimple_deleteButton__BUoAl")]',
    )
    
    DELETE_BUTTON = (
        By.XPATH,
        '//span[contains(@class, "vkuiButton__content") and text()="Удалить"]',
    )
    MODAL_DISMISS_BUTTON = (
        By.XPATH,
        '//div[contains(@class, "vkuiModalDismissButton")]',
    )