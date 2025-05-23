import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
  driver = webdriver.Firefox()
  driver.maximize_window()
  yield driver
  driver.quit()

def test_purchase(driver):
  driver.get("https://www.saucedemo.com/")

  username_field = driver.find_element(By.ID, "user-name")
  password_field = driver.find_element(By.ID, "password")
  login_button = driver.find_element(By.ID, "login-button")

  username_field.send_keys("standard_user")
  password_field.send_keys("secret_sauce")
  login_button.click()

  backpack_add_button = driver.find_element(By.XPATH,"//div[@class='inventory_item' and .//div[contains(text(), 'Sauce Labs Backpack')]]//button")
  tshirt_add_button = driver.find_element(By.XPATH,"//div[@class='inventory_item' and .//div[contains(text(), 'Sauce Labs Bolt T-Shirt')]]//button")
  onesie_add_button = driver.find_element(By.XPATH,"//div[@class='inventory_item' and .//div[contains(text(), 'Sauce Labs Onesie')]]//button")

  backpack_add_button.click()
  tshirt_add_button.click()
  onesie_add_button.click()

  cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
  cart_link.click()

  checkout_button = driver.find_element(By.ID, "checkout")
  checkout_button.click()

  first_name_field = driver.find_element(By.ID, "first-name")
  last_name_field = driver.find_element(By.ID, "last-name")
  postal_code_field = driver.find_element(By.ID, "postal-code")

  first_name_field.send_keys("Елена")
  last_name_field.send_keys("Пономаренко")
  postal_code_field.send_keys("193231")

  continue_button = driver.find_element(By.ID, "continue")
  continue_button.click()

  total_cost = driver.find_element(By.CLASS_NAME,"summary_total_label").text
  total_cost_value = float(total_cost.split("$")[1])

  assert total_cost_value == 58.29, f"Итоговая сумма должна быть 58.29,но получена {total_cost_value}"