import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from calculator_page import SlowCalculatorPage

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