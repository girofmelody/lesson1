from selenium.webdriver.common.by import By

class CartPage:
  def __init__(self, driver):
    self.driver = driver

  def proceed_to_checkout(self):
    checkout_button = self.driver.find_element(By.ID, "checkout")
    checkout_button.click()