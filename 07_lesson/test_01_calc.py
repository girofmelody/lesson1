import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SlowCalculatorPage:
  def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 60)
    self.delay_input_locator = (By.CSS_SELECTOR, '#delay')
    self.result_display_locator = (By.CSS_SELECTOR, '.screen')
    self.button_xpath_template = "//span[text() = '{}']"

  def open(self, url):
    self.driver.get(url)
    self.wait.until(EC.visibility_of_element_located(self.delay_input_locator))

  def set_delay(self, seconds):
    delay_input = self.driver.find_element(*self.delay_input_locator)
    delay_input.clear()
    delay_input.send_keys(str(seconds))

  def click_button(self, label):
    button_xpath = self.button_xpath_template.format(label)
    button = self.driver.find_element(By.XPATH, button_xpath)
    button.click()

  def get_result(self):
    result_element = self.driver.find_element(*self.result_display_locator)

    return result_element.text

@pytest.fixture
def driver():
  driver_instance = webdriver.Chrome()
  driver_instance.maximize_window()
  yield driver_instance
  driver_instance.quit()

def test_slow_calculator(driver):
  calculator_page = SlowCalculatorPage(driver)
  calculator_page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

  calculator_page.set_delay(45)

  calculator_page.click_button('7')
  calculator_page.click_button('+')
  calculator_page.click_button('8')
  calculator_page.click_button('=')

  wait = WebDriverWait(driver, 45)
  wait.until(EC.text_to_be_present_in_element(calculator_page.result_display_locator, '15'))

  result = calculator_page.get_result()
  assert result == "15"