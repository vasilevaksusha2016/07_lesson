from selenium.webdriver.common.by import By


class MakingOrderShopPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/checkout-step-one.html")
        self.first_name_locator = "first-name"
        self.last_name_locator = "last-name"
        self.poastal_code_locator = "postal-code"
        self.continue_locator = "continue"
        self.total_price_locator = "div.summary_total_label"

    def fill_form(self, first_name="Анастасия", last_name="Васильева",
                  postal_code="428038"):
        first_name_input = self._driver.find_element(
            By.ID, self.first_name_locator)
        first_name_input.send_keys(first_name)

        last_name_input = self._driver.find_element(
            By.ID, self.last_name_locator)
        last_name_input.send_keys(last_name)

        postal_code_input = self._driver.find_element(
            By.ID, self.poastal_code_locator)
        postal_code_input.send_keys(postal_code)

    def continue_input(self):
        self._driver.find_element(By.ID, self.continue_locator).click()

    def total_price(self):
        price = self._driver.find_element(
            By.CSS_SELECTOR, self.total_price_locator)
        return price.text
