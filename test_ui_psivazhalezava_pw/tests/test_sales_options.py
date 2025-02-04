import pytest


def test_hoodies_sales(sales_page):
    sales_page.open_page()
    sales_page.check_women_hoodies_title_and_breadcrumbs()


@pytest.mark.parametrize("search_options", ['pants', 'men', 'women'])
def test_search_positive(sales_page, search_options):
    sales_page.open_page()
    sales_page.search_items(search_options)
    expected_text = f"Search results for: '{search_options}'"
    assert search_options in expected_text, f"Expected text '{search_options}' not found in '{expected_text}'"


def test_search_no_results_error(sales_page):
    sales_page.open_page()
    sales_page.search_items('aaa')
    sales_page.verify_error_text('Your search returned no results.')


def test_search_minimum_length_error(sales_page):
    sales_page.open_page()
    sales_page.search_items('a')
    sales_page.verify_error_text('Minimum Search query length is 3')
