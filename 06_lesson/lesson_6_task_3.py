from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
  driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

  images = WebDriverWait(driver, 20).until(

  EC.presence_of_element_located((By.ID, "landscape"))
  )

  find= WebDriverWait(driver, 20)
  award_element = find.until(EC.presence_of_element_located((By.ID, "award")))
  src = award_element.get_attribute("src")
  print(src)

finally:
  driver.quit()