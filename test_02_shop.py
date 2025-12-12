import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.AuthorizationShopPage import AuthorizationPage
from pages.MainToCartShopPage import MainToCartShopPage
from pages.CartShopPage import CartShopPage
from pages.MakingOrderShopPage import MakingOrderShopPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.quit()


def test_shop(driver):
    authorization_page = AuthorizationPage(driver)
    authorization_page.open()
    authorization_page.auth_form()
    authorization_page.submit_form()

    main_to_cart_shop_page = MainToCartShopPage(driver)
    main_to_cart_shop_page.adding_product()
    main_to_cart_shop_page.transfer_cart()

    cart_shop_page = CartShopPage(driver)
    cart_shop_page.button_checkout

    making_order_shop_page = MakingOrderShopPage(driver)
    making_order_shop_page.fill_form()
    making_order_shop_page.continue_input()
    making_order_shop_page.total_price()

    final_total_price = making_order_shop_page.total_price()
    assert final_total_price == 'Total: $58.29'
