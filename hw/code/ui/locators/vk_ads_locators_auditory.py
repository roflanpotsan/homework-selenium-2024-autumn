from selenium.webdriver.common.by import By


class AuditoryPageLocators:
    CREATE_AUDIENCE_BUTTON = (By.CSS_SELECTOR, '[data-testid="create-audience"]')
    AUDITORY_NAME = (
        By.XPATH,
        '//div[h5//div[text()="Название"]]//input[@type="text"]',
    )

    ADD_SOURCE_BUTTON = (By.XPATH, '//button[.//span[text()="Включить источник"]]')
    KEY_REFRASE_BUTTON = (
        By.XPATH,
        '//div[contains(@class, "vkuiSimpleCell") and .//span[text()="Ключевые фразы"]]',
    )

    KEY_PHRASE_TEXTAREA = (
        By.XPATH,
        '//label[text()="Ключевые фразы"]/ancestor::div[contains(@class, "vkuiFormItem")]//textarea',
    )
    MINUS_PHRASE_TEXTAREA = (
        By.XPATH,
        '//label[text()="Минус-фразы"]/ancestor::div[contains(@class, "vkuiFormItem")]//textarea',
    )
    SAVE_KEY_PHRASES_BUTTON = (
        By.XPATH,
        '//button[@data-testid="submit" and contains(@class, "vkuiButton--mode-primary")]',
    )
    AUDITORY_CHECKBOX = (
        By.XPATH,
        '//h5[text()="Аудитория"]/ancestor::div[contains(@class, "BaseTable__row")]//input[@type="checkbox"]',
    )
    DELETE_AUDIENCE_BUTTON = (By.CSS_SELECTOR, '[data-testid="remove-items-button"]')
    DELETE_BUTTON = (
        By.XPATH,
        '//button[contains(@class, "vkuiButton") and .//span[contains(@class, "vkuiButton__content") and text()="Удалить"]]',
    )
    CREATE_AUDIENCE_SOURCE_MODAL = (
        By.XPATH,
        '//div[contains(@class, "ModalRoot_overlay__")]',
    )
    SUBMIT_BTN = (By.CSS_SELECTOR, "[data-testid=submit]")
    AUDIENCE_CHECKBOX = (
        By.XPATH,
        "//div[contains(@class, 'vkuiCheckbox__icon') and contains(@class, 'vkuiCheckbox__icon--off')]",
    )

    SHARE_AUDIENCE_BUTTON = (By.XPATH, "//button[@data-testid='share-button']")
