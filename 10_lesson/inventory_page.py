from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class InventoryPage:
  """
  Класс, представляющий страницу инвентаря.

  Attributes:
    driver (WebDriver): Экземпляр веб-драйвера, используемый для взаимодействия с браузером.
  """

  def __init__(self, driver: WebDriver):
    """
    Инициализирует класс InventoryPage.

    Parameters:
      driver (WebDriver): Экземпляр веб-драйвера для управления браузером.
    """
    self.driver = driver

  def add_product_to_cart(self, product_name: str) -> None:
    """
    Добавляет продукт в корзину по его имени.

    Parameters:
      product_name (str): Имя продукта, который необходимо добавить в корзину.

    Returns:
      None: Метод не возвращает значение.
    """
    products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
    for product in products:
      name_element = product.find_element(By.CLASS_NAME,"inventory_item_name")
      if name_element.text == product_name:
          add_button = product.find_element(By.CLASS_NAME,"btn_inventory")
          add_button.click()
          break

  def go_to_cart(self):
    """
        Метод для перехода на страницу корзины

        Returns:
          None: Метод не возвращает значение.
        """
    cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()
    