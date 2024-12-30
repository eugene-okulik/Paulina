from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.set_window_size(1020, 1080)
    yield chrome_driver


def test_language(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    languages_list = driver.find_element(By.NAME, 'choose_language')
    languages_list.click()
    option_select = driver.find_element(By.XPATH, '//option[@value="1"]')
    option_text = option_select.text
    option_select.click()
    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.click()
    displayed_text = driver.find_element(By.ID, 'result-text').text
    assert option_text == displayed_text


def test_button(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_button = driver.find_element(By.TAG_NAME, 'button')
    start_button.click()
    wait = WebDriverWait(driver, 20)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@id='finish']/child::h4")
        )
    )
    hello_world_element = driver.find_element(By.XPATH, "//div[@id='finish']/child::h4").text
    print(hello_world_element)
    assert hello_world_element == 'Hello World!'
