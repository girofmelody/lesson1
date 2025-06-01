from selenium.webdriver.common.by import By

class InventoryPage:
  def __init__(self, driver):
    self.driver = driver

  def add_product_to_cart(self, product_name):
    products = self.driver.find_elements(
      By.CLASS_NAME, "inventory_item"
  )
    for product in products:
      name_element = product.find_element(
        By.CLASS_NAME, "inventory_item_name"
      )
      if name_element.text == product_name:
        add_button = product.find_element(
          By.CLASS_NAME, "btn_inventory"
        )
        add_button.click()
        break

  def go_to_cart(self):
    cart_icon = self.driver.find_element(
      By.CLASS_NAME, "shopping_cart_link"
    )
    cart_icon.click()