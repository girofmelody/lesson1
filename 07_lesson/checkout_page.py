from selenium.webdriver.common.by import By

class CheckoutPage:
  def __init__(self, driver):
    self.driver = driver

  def fill_in_details(self, first_name, last_name, postal_code):
    self.driver.find_element(By.ID, "first-name").send_keys(first_name)
    self.driver.find_element(By.ID, "last-name").send_keys(last_name)
    self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

  def continue_checkout(self):
    continue_button = self.driver.find_element(By.ID, "continue")
    continue_button.click()

  def get_total_cost(self):
    total_element = self.driver.find_element(
    By.CLASS_NAME, "summary_total_label"
    )
    total_text = total_element.text
    total_value_str = total_text.split('$')[-1]

    return float(total_value_str)