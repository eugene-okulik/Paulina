from test_ui_psivazhalezava_pw.pages.base_page import BasePage
from test_ui_psivazhalezava_pw.pages.locators.eco_friendly_locators import EcoFriendlyLocators as Loc
from playwright.sync_api import expect


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html/'

    def check_default_pagination_option(self):

        default_pagination_option = self.find(Loc.pagination_option_default_loc)
        expected_quantity = int(default_pagination_option.inner_text().strip())
        cards_locator = self.find(Loc.cards_loc)
        expect(cards_locator).to_have_count(expected_quantity)

    def select_xs_size_and_check_items_labels(self):
        self.find(Loc.filter_size_loc).click()
        select_xs_option = self.find(Loc.xs_option_size_loc)
        expect(select_xs_option).to_have_text('XS')
        select_xs_option.click()
        filter_label = self.find(Loc.filter_label_loc)
        filtered_cards_texts = [card.inner_text() for card in self.find(Loc.filtered_cards_loc).element_handles()]
        for text in filtered_cards_texts:
            assert 'XS' in text
        expect(filter_label).to_have_text('XS')

    def clear_filter(self):
        self.find(Loc.clear_filter_loc).click()

    def filter_price_and_check_items_price_is_in_range(self):
        self.find(Loc.filter_price_loc).click()
        self.find(Loc.price_option_loc).click()
        product_prices = [float(price.inner_text().replace("$", "")) for price in
                          self.find(Loc.products_prices_loc).element_handles()]
        for price in product_prices:
            assert 10.00 <= price <= 19.99
