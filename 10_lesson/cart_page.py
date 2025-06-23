from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CartPage:
  """
  Класс, представляющий страницу корзины.

  Attributes:
    driver (WebDriver): Экземпляр веб-драйвера,
    используемый для взаимодействия с браузером.
  """

  def __init__(self, driver: WebDriver):
    """
    Инициализирует класс CartPage.

    Parameters:
      driver (WebDriver): Экземпляр веб-драйвера
      для управления браузером.
    """
    self.driver = driver

  def proceed_to_checkout(self) -> None:
    """
    Переходит к процессу оформления заказа, нажимая на кнопку "Checkout".
    Returns:
      None: Метод не возвращает значение.
    """

    checkout_button = self.driver.find_element(By.ID, "checkout")
    checkout_button.click()