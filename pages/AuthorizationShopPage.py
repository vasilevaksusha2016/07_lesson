from selenium.webdriver.common.by import By


class AuthorizationPage:
    def __init__(self, driver):
        self._driver = driver
        self.name_locator = "user-name"
        self.password_locator = "password"
        self.login_locator = "login-button"

    def open(self):
        self._driver.get("https://www.saucedemo.com/")

    def auth_form(self, username="standard_user", password="secret_sauce"):
        name_input = self._driver.find_element(
            By.ID, self.name_locator)
        name_input.send_keys(username)

        password_input = self._driver.find_element(
            By.ID, self.password_locator)
        password_input.send_keys(password)

    def submit_form(self):
        self._driver.find_element(By.ID, self.login_locator).click()
