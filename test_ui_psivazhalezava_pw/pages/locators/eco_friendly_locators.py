class EcoFriendlyLocators:
    pagination_drop_down_loc = '//*[@id="limiter"]'
    cards_loc = '//li[@class="item product product-item"]'
    filter_size_loc = "(//div[@class='filter-options-title' and @tabindex='0'])[3]"
    xs_option_size_loc = "//a[@aria-label='XS']//div[contains(@class, 'swatch-option')]"
    filter_label_loc = "//li[contains(@class, 'item')]//span[@class='filter-value']"
    clear_filter_loc = 'a.action.clear.filter-clear'
    filtered_cards_loc = "//div[contains(@class, 'swatch-option') and @option-label='XS' and @aria-label='XS']"
    pagination_option_default_loc = '//main/div[3]/div[1]/div[4]/div[3]/div/select/option[1]'
    filter_price_loc = "(//div[@class='filter-options-title' and @tabindex='0'])[12]"
    price_option_loc = "a[href*='eco-friendly.html?price=10-20']"
    products_prices_loc = "//li[@class='item product product-item']//span[@class='price']"
