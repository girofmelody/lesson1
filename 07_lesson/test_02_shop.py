import pytest
from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage

@pytest.fixture(scope="function")
def driver():
  driver = webdriver.Firefox()
  driver.maximize_window()
  yield driver
  driver.quit()

def test_purchase(driver):
  driver.get("https://www.saucedemo.com/")

  login_page = LoginPage(driver)
  inventory_page = InventoryPage(driver)
  cart_page = CartPage(driver)
  checkout_page = CheckoutPage(driver)

  login_page.login("standard_user", "secret_sauce")

  products_to_add = [
      "Sauce Labs Backpack",
      "Sauce Labs Bolt T-Shirt",
      "Sauce Labs Onesie"
    ]

  for product in products_to_add:
      inventory_page.add_product_to_cart(product)

  inventory_page.go_to_cart()

  cart_page.proceed_to_checkout()

  checkout_page.fill_in_details("Алена", "Пономаренко", "193231")

  checkout_page.continue_checkout()

  total_cost_value = checkout_page.get_total_cost()

  assert total_cost_value == 58.29, \
    f"Итоговая сумма должна быть 58.29, но получена {total_cost_value}"