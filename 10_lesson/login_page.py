from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
  """
  Класс, представляющий страницу входа в систему.

  Attributes:
    driver (WebDriver): Экземпляр веб-драйвера, используемый для взаимодействия с браузером.
    username_input (tuple): Локатор для поля ввода имени пользователя.
    password_input (tuple): Локатор для поля ввода пароля.
    login_button (tuple): Локатор для кнопки входа.
  """

  def __init__(self, driver: WebDriver):
    """
    Инициализирует класс LoginPage.

    Parameters:
      driver (WebDriver): Экземпляр веб-драйвера для управления браузером.
    """
    self.driver = driver
    self.username_input = (By.ID, "user-name")
    self.password_input = (By.ID, "password")
    self.login_button = (By.ID, "login-button")

  def login(self, username: str, password: str) -> None:
    """

    Выполняет вход в систему, используя предоставленные учетные данные.

    Parameters:
      username (str): Имя пользователя для входа.
      password (str): Пароль для входа.

    Returns:
      None: Метод не возвращает значение.
    """
    self.driver.find_element(*self.username_input).send_keys(username)
    self.driver.find_element(*self.password_input).send_keys(password)
    self.driver.find_element(*self.login_button).click()