from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

try:
  driver.get("http://the-internet.herokuapp.com/inputs")

  input_field = driver.find_element(By.TAG_NAME, "input")
  input_field.send_keys("Sky")

  time.sleep(2)
  input_field.clear()

  input_field.send_keys("Pro")

  time.sleep(2)

finally:
    driver.quit()