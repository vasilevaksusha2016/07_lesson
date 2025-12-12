from selenium.webdriver.common.by import By


class CartShopPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/cart.html")
        self.checkout_button = "checkout"

    def button_checkout(self):
        self._driver.find_element(By.ID, self.checkout_button).click()
