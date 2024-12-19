from ads_vk_test_base import BaseCase
class TestCommersion(BaseCase):
    authorize = True

    def navigate_to_commersion(self):
        self.landing_page.login()
        self.landing_page.open_profile()
        self.landing_page.wait(15).until(lambda driver: driver.current_url == 'https://ads.vk.com/hq/overview')
        self.commersion_page.click(self.landing_page.locators.COMMERSION_LINK)

    def test_create_and_delete_catalog(self):
        self.navigate_to_commersion()
        self.commersion_page.click_dismiss_modal_button()
        self.commersion_page.click_create_catalog_button()
        self.commersion_page.fill_input(self.commersion_page.locators.NAME_INPUT, "New catalog")
        self.commersion_page.click_feed_button()
        self.commersion_page.fill_input(self.commersion_page.locators.FEED_INPUT, "https://vk.com/archstudios")
        print("before")
        self.commersion_page.click_create_button()
        self.commersion_page.click_catalog_goods_tab()
        self.commersion_page.click_catalog_goods_tab_settings()
        self.commersion_page.click_catalog_goods_tab_checkbox()
        self.commersion_page.click_catalog_goods_tab_confirm()

        self.commersion_page.click_catalog_groups_tab()
        self.commersion_page.click_catalog_groups_tab_create()
        self.commersion_page.click_catalog_groups_tab_filters()
        self.commersion_page.fill_input(self.commersion_page.locators.CATALOG_TAB_GROUPS_CREATE_BY_FILTERS_INPUT_NAME, "New group")
        self.commersion_page.fill_input(self.commersion_page.locators.CATALOG_TAB_GROUPS_CREATE_BY_FILTERS_INPUT_VALUE, "8000")
        self.commersion_page.click_catalog_groups_tab_filters_confirm()

        # self.commersion_page.click_catalog_settings_button()
        # self.commersion_page.click_catalog_delete_button()
        # self.commersion_page.confirm_delete()
        # self.commersion_page.check_catalog_deleted()