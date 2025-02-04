from playwright.sync_api import BrowserContext
import pytest
from test_ui_psivazhalezava_pw.pages.eco_friendly_page import EcoFriendlyPage
from test_ui_psivazhalezava_pw.pages.sales_page import SalesPage
from test_ui_psivazhalezava_pw.pages.create_account_page import CreateAccount


@pytest.fixture()
def page(context: BrowserContext, playwright):
    playwright.selectors.set_test_id_attribute("id")
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def create_new_account_page(page):
    return CreateAccount(page)


@pytest.fixture()
def eco_friendly_page(page):
    return EcoFriendlyPage(page)


@pytest.fixture()
def sales_page(page):
    return SalesPage(page)
