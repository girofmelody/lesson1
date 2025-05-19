from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
  driver.get("http://uitestingplayground.com/ajax")

  blue_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
  blue_button.click()

  success_message = WebDriverWait(driver, 20).until(
  EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
  ).text

  print(success_message)

finally:
  driver.quit()