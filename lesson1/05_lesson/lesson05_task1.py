from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://uitestingplayground.com/classattr")
sleep(1)

driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

sleep(3)

alert = Alert(driver)
alert.accept()

sleep(3)