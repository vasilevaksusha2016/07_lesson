import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalculatorPage import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_form(driver):
    calc_page = CalculatorPage(driver)
    calc_page.open()
    calc_page.entering_delay()
    calc_page.button_click()

    calc_page.wait_for_result("15")
    result = calc_page.get_screen_text()
    assert result == "15"
