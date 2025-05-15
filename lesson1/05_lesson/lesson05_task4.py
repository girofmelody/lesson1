from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

try:
  driver.get("http://the-internet.herokuapp.com/login")

  username_field = driver.find_element(By.ID, "username")
  username_field.send_keys("tomsmith")

  password_field = driver.find_element(By.ID, "password")
  password_field.send_keys("SuperSecretPassword!")

  login_button = driver.find_element(By.CSS_SELECTOR, ".fa.fa-2x.fa-sign-in")
  login_button.click()

  time.sleep(2)

  success_message = driver.find_element(By.CSS_SELECTOR, "#flash").text
  print(success_message)

finally:
  driver.quit()