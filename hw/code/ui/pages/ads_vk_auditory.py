from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from ui.locators.vk_ads_locators_auditory import AuditoryPageLocators
from selenium.webdriver.common.by import By
from ui.pages.ads_vk_base import BasePage


class AuditoryPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        # self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)
        self.locators = AuditoryPageLocators

    # Метод для нажатия кнопки "Создать аудиторию"
    def click_create_audience_button(self):
        create_button = self.wait(timeout=5).until(
            EC.presence_of_element_located(self.locators.CREATE_AUDIENCE_BUTTON)
        )
        create_button.click()

    # Метод для заполнения поля ввода
    def fill_input_field(self, locator, value):
        input_field = self.wait(timeout=5).until(
            EC.presence_of_element_located(locator)
        )
        input_field.clear()
        input_field.send_keys(value)

    # Метод для нажатия кнопки "Добавить источник"
    def click_add_source_button(self):
        add_source_button = self.wait(timeout=5).until(
            EC.element_to_be_clickable(self.locators.ADD_SOURCE_BUTTON)
        )
        add_source_button.click()

    # Метод для нажатия кнопки "Ключевые фразы"
    def click_key_phrases_button(self):
        key_phrases_button = self.wait(timeout=5).until(
            EC.element_to_be_clickable(self.locators.KEY_REFRASE_BUTTON)
        )
        key_phrases_button.click()

    # Метод для сохранения ключевых фраз
    def click_save_key_phrases_button(self):
        self.find_all_presence(self.locators.SUBMIT_BTN)[1].click()

    # Метод для нажатия кнопки "Сохранить аудиторию"
    def click_save_audience_button(self):
        self.became_invisible(self.locators.CREATE_AUDIENCE_SOURCE_MODAL, 1)
        self.find(self.locators.SUBMIT_BTN, 2).click()

    # Методы для выбора чекбокса аудитории
    def click_audience_checkbox(self):
        try:
            self.click(self.locators.AUDIENCE_CHECKBOX, timeout=10)
        except Exception as e:
            print(f"Error occurred while clicking audience checkbox: {e}")

    def check_share_audience_button_active(self):
        try:
            self.find(self.locators.SHARE_AUDIENCE_BUTTON, timeout=10)
        except Exception as e:
            print(f"Error occurred while checking share audience button active: {e}")


    # Метод для нажатия кнопки "Удалить"
    def click_delete_audience_button(self):
        delete_button = self.wait(timeout=5).until(
            EC.element_to_be_clickable(self.locators.DELETE_AUDIENCE_BUTTON)
        )
        delete_button.click()

    # Метод для подтверждения удаления
    def confirm_delete(self):
        confirm_button = self.wait(timeout=5).until(
            EC.element_to_be_clickable(self.locators.DELETE_BUTTON)
        )
        confirm_button.click()
