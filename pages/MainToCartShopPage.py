from selenium.webdriver.common.by import By


class MainToCartShopPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/inventory.html")
        self.cart_button = "a.shopping_cart_link"
        self.products = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]

    def adding_product(self):
        for products in self.products:
            self._driver.find_element(By.ID, products).click()

    def transfer_cart(self):
        self._driver.find_element(
            By.CSS_SELECTOR, self.cart_button).click()
