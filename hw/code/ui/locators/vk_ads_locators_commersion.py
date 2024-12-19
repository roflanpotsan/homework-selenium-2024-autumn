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

    CATALOG_TAB_GOODS = (By.CSS_SELECTOR, '[data-testid="catalog-tabs-goods"]')

    CATALOG_TAB_GOODS_SETTINGS = (
        By.XPATH,
        '//button[contains(@class, "TableSettings_settingsButton__uz8xK")]',
    )

    CATALOG_TAB_GOODS_SETTINGS_CHECKBOX = (
        By.XPATH,
        '//span[text()="Наличие"]',
    )

    CATALOG_TAB_GOODS_SETTINGS_CONFIRM = (
        By.XPATH,
        '//span[text()="Применить"]',
    )

    CATALOG_TAB_GROUPS = (By.CSS_SELECTOR, '[data-testid="catalog-tabs-groups"]')

    CATALOG_TAB_GROUPS_CREATE = (
        By.XPATH,
        '//span[text()="Создать группу"]',
    )

    CATALOG_TAB_GROUPS_CREATE_BY_FILTERS = (
        By.XPATH,
        '//span[text()="Использовать фильтры"]',
    )

    CATALOG_TAB_GROUPS_CREATE_BY_FILTERS_INPUT_NAME = (
        By.XPATH,
        '//input[@name="groupName"]',
    )

    CATALOG_TAB_GROUPS_CREATE_BY_FILTERS_INPUT_VALUE = (
        By.XPATH,
        '//div[@class="vkuiFormItem vkuiFormItem--withPadding vkuiInternalFormItem vkuiFormItem--sizeY-none vkuiInternalFormItem--sizeY-none Condition_formItem__Obi-n Condition_conditionValue__zV0Wg"]//input[@type="text"]',
    )

    CATALOG_TAB_GROUPS_CREATE_BY_FILTERS_CONFIRM = (
        By.XPATH,
        '//span[text()="Сохранить"]',
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
    CATALOGS_TABLE = (
        By.XPATH,
        '//div[contains(@class, "table_table__2JcCk")]',
    )