import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalcPage import CalcPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_form(driver):
    calc_page = CalcPage(driver)
    calc_page.open()
    calc_page.entering_delay()
    calc_page.button_calc()
    calc_page.result_field()
