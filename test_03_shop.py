import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.shop.AuthorizationPage import AuthorizationPage
from pages.shop.MainToCartPage import MainToCartPage
from pages.shop.CartPage import CartPage
from pages.shop.MakingOrderPage import MakingOrderPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.quit()


def test_shop(driver):
    authorization_page = AuthorizationPage(driver)
    authorization_page.open()
    authorization_page.fill_form()
    authorization_page.submit_form()

    main_to_cart_page = MainToCartPage(driver)
    main_to_cart_page.adding_product()
    main_to_cart_page.transfer_cart()

    cart_page = CartPage(driver)
    cart_page.button_checkout

    making_order_page = MakingOrderPage(driver)
    making_order_page.fill_form()
    making_order_page.total_price_text()
