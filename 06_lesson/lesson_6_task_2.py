from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
  driver.get("http://uitestingplayground.com/textinput")
  input_field = driver.find_element(By.ID, "newButtonName")
  input_field.send_keys("SkyPro")

  blue_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
  blue_button.click()

  # Ожидание изменения текста кнопки
  WebDriverWait(driver, 60).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".btn.btn-primary"), "SkyPro")
  )

  button_text = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").text
  print(button_text)

finally:
  driver.quit()