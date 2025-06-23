import pytest
import allure
from selenium import webdriver
#from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from slow_calculator_page import SlowCalculatorPage

@pytest.fixture
def driver():
  driver_instance = webdriver.Chrome()
  driver_instance.maximize_window()
  yield driver_instance
  driver_instance.quit()

@allure.feature("Калькулятор")
@allure.title("Тест медленного калькулятора")
@allure.description("Проверка работы медленного калькулятора с задержкой")
@allure.severity(allure.severity_level.CRITICAL)

def test_slow_calculator(driver):
  calculator_page = SlowCalculatorPage(driver)
  with (((((((allure.step("Открываем страницу калькулятора")))))))):
    calculator_page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
  with allure.step("Устанавливаем задержку в 45 секунд"):
    calculator_page.set_delay(45)
  with allure.step("Нажимаем кнопки для вычисления 7 + 8"):
    calculator_page.click_button('7')
    calculator_page.click_button('+')
    calculator_page.click_button('8')
    calculator_page.click_button('=')

  wait = WebDriverWait(driver, 45)
  with allure.step("Ожидаем, что результат станет 15"):
    wait.until(EC.text_to_be_present_in_element
      (calculator_page.result_display_locator, '15'))

  with allure.step("Получаем результат вычисления"):
    result = calculator_page.get_result()

  with allure.step("Проверяем, что результат равен 15"):
    assert result == "15"