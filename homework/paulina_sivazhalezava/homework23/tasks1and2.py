from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.set_window_size(420, 900)
    yield chrome_driver


def test_text_input(driver):
    input_data = 'mistercat'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.NAME, 'text_string')
    text_string.send_keys(input_data)
    text_string.send_keys(Keys.ENTER)
    print(driver.find_element(By.ID, "result-text").text)


def test_filling_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    firstname = driver.find_element(By.ID, 'firstName')
    firstname.send_keys('Kot')
    lastname = driver.find_element(By.ID, 'lastName')
    lastname.send_keys('Usaty')
    email = driver.find_element(By.ID, 'userEmail')
    email.send_keys('kotsuslik@mmail.com')
    wait = WebDriverWait(driver, 20)
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@value="Male"]/following::label[@for="gender-radio-1"]')
        )
    )
    gender = driver.find_element(By.XPATH, '//*[@value="Male"]/following::label[@for="gender-radio-1"]')
    gender.click()
    mobile = driver.find_element(By.ID, 'userNumber')
    mobile.send_keys('5551115551')
    driver.execute_script("window.scrollTo(0, 400)")
    wait.until(
        EC.element_to_be_clickable(
            driver.find_element(By.XPATH, '//*[@id="dateOfBirthInput"]')
        )
    )
    date_of_birth = driver.find_element(By.XPATH, '//*[@id="dateOfBirthInput"]')
    date_of_birth.click()
    selecting_month = driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
    selecting_month.click()
    month = driver.find_element(By.XPATH, '//option[@value=10]')
    month.click()
    selecting_year = driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
    selecting_year.click()
    year = driver.find_element(By.XPATH, '//option[@value=2000]')
    year.click()
    date = driver.find_element(By.XPATH, '//div[@aria-label="Choose Sunday, November 5th, 2000"]')
    date.click()
    subjects = driver.find_element(By.ID, "subjectsInput")
    subjects.send_keys('Chemistry')
    subjects.send_keys(Keys.ENTER)
    driver.execute_script("window.scrollTo(400, 600)")
    hobby = driver.find_element(By.XPATH,
                                "//input[@id='hobbies-checkbox-1']/following::label[@for='hobbies-checkbox-1']")
    hobby.click()
    address = driver.find_element(By.ID, 'currentAddress')
    address.send_keys('345 Baker street')
    driver.execute_script("window.scrollTo(700, 900)")
    country = driver.find_element(By.ID, 'state')
    country.click()
    enter_country = driver.find_element(By.ID, "react-select-3-input")
    enter_country.send_keys("NCR")
    enter_country.send_keys(Keys.ENTER)
    city = driver.find_element(By.ID, 'city')
    city.click()
    enter_city = driver.find_element(By.ID, "react-select-4-input")
    enter_city.send_keys("Delhi")
    enter_city.send_keys(Keys.ENTER)
    submit_form = driver.find_element(By.ID, 'submit')
    submit_form.click()
    retrieve_submitted = driver.find_elements(By.TAG_NAME, 'td')
    for element in retrieve_submitted:
        print(element.get_attribute('innerText'))
