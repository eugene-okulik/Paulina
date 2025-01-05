from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_phones(driver):
    driver.get('https://www.demoblaze.com/index.html')
    wait = WebDriverWait(driver, 20)
    select_category = driver.find_element(By.LINK_TEXT, "Phones")
    select_category.click()
    driver.implicitly_wait(10)
    all_phones = driver.find_elements(By.XPATH, "//*[@class='hrefch']")
    one_phone = all_phones[0]
    wait.until(
        EC.element_to_be_clickable(
            one_phone
        )
    )
    ActionChains(driver).key_down(Keys.COMMAND).click(one_phone).key_up(Keys.COMMAND).perform()
    driver.implicitly_wait(10)
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    add_to_card_button = driver.find_element(By.XPATH, "//*[@onclick='addToCart(1)']")
    add_to_card_button.click()
    driver.implicitly_wait(20)
    alert = Alert(driver)
    wait.until(
        EC.alert_is_present(
        )
    )
    alert.accept()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[0])
    cart = driver.find_element(By.LINK_TEXT, "Cart")
    cart.click()
    retrieve_added = driver.find_elements(By.TAG_NAME, 'td')
    fetch_text = retrieve_added[1].get_attribute('innerText')
    print(fetch_text)
    assert fetch_text == 'Samsung galaxy s6'


def test_bags(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    bag = driver.find_element(By.XPATH,
                              "//*[@data-product-id='14']")
    actions = ActionChains(driver)
    actions.move_to_element(bag)
    driver.implicitly_wait(5)
    add_compare = driver.find_element(By.XPATH,
                                      '//*[@data-product-id="14"]/following::a[@aria-label="Add to Compare"]')
    actions.click(add_compare)
    actions.perform()
    compare_list = driver.find_element(By.XPATH, "//*[@value='14']/following::strong[@class='product-item-name']")
    assert compare_list.get_attribute('innerText') == 'Push It Messenger Bag'
