from test_base import BaseCase

class TestAuditory(BaseCase):
    authorize = True
    
    def navigate_to_auditory(self):
        self.landing_page.login()
        self.landing_page.open_profile()
        self.landing_page.wait(15).until(lambda driver: driver.current_url == 'https://ads.vk.com/hq/overview')
        self.budget_page.click(self.landing_page.locators.AUDITORY_LINK)
    

    def test_create_and_delete_audience(self):
        self.navigate_to_auditory()
        # Нажимаем на кнопку "Создать аудиторию"
        self.auditory_page.click_create_audience_button()
        self.auditory_page.fill_input_field(self.auditory_page.locators.AUDITORY_NAME, "Аудитория")
        self.auditory_page.click_add_source_button()
        self.auditory_page.click_key_phrases_button()
        # Заполняем поле "Ключевые фразы" и "Минус-фразы"
        self.auditory_page.fill_input_field(self.auditory_page.locators.KEY_PHRASE_TEXTAREA, "Пример ключевой фразы")
        self.auditory_page.fill_input_field(self.auditory_page.locators.MINUS_PHRASE_TEXTAREA, "Пример минус-фразы")

        # Сохраняем ключевые фразы
        self.auditory_page.click_save_key_phrases_button()

        # Нажимаем на кнопку "Сохранить аудиторию"
        self.auditory_page.click_save_audience_button()

        # Выбираем чекбокс созданной аудитории
        # self.auditory_page.select_audience_checkbox()
        self.auditory_page.click_audience_checkbox()
        self.auditory_page.check_share_audience_button_active()
        # Удаляем аудиторию
        self.auditory_page.click_delete_audience_button()
        self.auditory_page.confirm_delete()
