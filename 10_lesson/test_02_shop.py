import pytest
from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage
import allure

@pytest.fixture(scope="function")
def driver() -> webdriver:
  """
  Fixture для создания экземпляра драйвера Chrome.

  Returns:
    webdriver.Chrome: Экземпляр драйвера Chrome.
  """
  driver = webdriver.Firefox()

  driver.maximize_window()
  yield driver
  driver.quit()

@allure.title("Тест покупки товаров")
@allure.description("Тестирует процесс покупки товаров на сайте SauceDemo.")
@allure.feature("Покупка товаров")
@allure.severity(allure.severity_level.CRITICAL)

def test_purchase(driver) -> None:
  """
  Тестирует процесс покупки товаров на сайте SauceDemo.

  Args:
    driver (webdriver.Chrome): Экземпляр драйвера Chrome.

  Returns:
    None
  """
  driver.get("https://www.saucedemo.com/")

  login_page = LoginPage(driver)
  inventory_page = InventoryPage(driver)
  cart_page = CartPage(driver)
  checkout_page = CheckoutPage(driver)

  with allure.step("Вход в систему"):
    login_page.login("standard_user", "secret_sauce")

  products_to_add = [
    "Sauce Labs Backpack",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Onesie"
  ]

  for product in products_to_add:
    with allure.step("Добавление товара '{product}' в корзину"):
      inventory_page.add_product_to_cart(product)

  with allure.step("Переход в корзину"):
    inventory_page.go_to_cart()

  with allure.step("Переход к оформлению заказа"):
    cart_page.proceed_to_checkout()

  with allure.step("Заполнение данных для оформления заказа"):
    checkout_page.fill_in_details("Алена", "Пономаренко", "193231")

  with allure.step("Продолжение оформления заказа"):
    checkout_page.continue_checkout()

  with allure.step("Получение итоговой суммы"):
    total_cost_value = checkout_page.get_total_cost()

  with allure.step("Проверка итоговой суммы"):
    assert total_cost_value == 58.29, \
      (f"Итоговая сумма должна быть 58.29,"
      f"но получена {total_cost_value}")