from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CheckoutPage:
  """
  Класс, представляющий страницу оформления заказа.

  Attributes:
    driver (WebDriver): Экземпляр веб-драйвера,используемый для взаимодействия с браузером.
  """

  def __init__(self, driver: WebDriver):
    """
    Инициализирует класс CheckoutPage.

    Parameters:
      driver (WebDriver): Экземпляр веб-драйвера для управления браузером.
    """
    self.driver = driver

  def fill_in_details(self, first_name: str,
        last_name: str, postal_code: str) -> None:
    """
    Заполняет форму с деталями пользователя.

    Parameters:
      first_name (str): Имя пользователя.
      last_name (str): Фамилия пользователя.
      postal_code (str): Почтовый индекс пользователя.

    Returns:
      None: Метод не возвращает значение.
    """
    self.driver.find_element(By.ID, "first-name").send_keys(first_name)
    self.driver.find_element(By.ID, "last-name").send_keys(last_name)
    self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

  def continue_checkout(self) -> None:
    """
    Переходит к следующему шагу оформления заказа,нажимая на кнопку "Continue".

    Returns:
      None: Метод не возвращает значение.
    """
    continue_button = self.driver.find_element(By.ID, "continue")
    continue_button.click()

  def get_total_cost(self) -> float:
    """
    Получает общую стоимость заказа.

    Returns:
      float: Общая стоимость заказа как число с плавающей запятой.
    """
    total_element = self.driver.find_element(By.CLASS_NAME,"summary_total_label")
    total_text = total_element.text
    total_value_str = total_text.split('$')[-1]
    return float(total_value_str)
