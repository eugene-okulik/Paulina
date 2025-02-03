from test_ui_psivazhalezava_pw.pages.base_page import BasePage
from test_ui_psivazhalezava_pw.pages.locators.sales_locators import SalesLocators as Loc
from playwright.sync_api import expect


class SalesPage(BasePage):
    page_url = '/sale.html'

    def check_women_hoodies_title_and_breadcrumbs(self):
        self.find(Loc.hoodies_link_loc).click()
        expect(self.find(Loc.hoodies_title_loc)).to_have_text('Hoodies & Sweatshirts')

        breadcrumbs_elements = [element.inner_text() for element in
                                self.find(Loc.hoodies_breadcrumbs_loc).element_handles()]
        print(breadcrumbs_elements)
        expected_breadcrumbs = ['Home  Women  Tops  Hoodies & Sweatshirts']
        assert breadcrumbs_elements == expected_breadcrumbs

    def search_items(self, text):
        search_field = self.find(Loc.search_field_loc)
        search_field.fill(text)
        search_field.press('Enter')

        result_text = self.find(Loc.page_title_after_search_loc).inner_text()
        return result_text

    def verify_error_text(self, error_text_expected):
        error_text = self.find(Loc.error_loc).inner_text().split('\n')[0].strip()
        assert error_text == error_text_expected