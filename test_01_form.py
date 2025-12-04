import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from pages.FormPage import FormPage


@pytest.fixture
def driver():
    edge_driver = (
        r"C:\Users\user\Desktop\Edge\edgedriver_win32\msedgedriver.exe")
    driver = webdriver.Edge(service=EdgeService(edge_driver))
    yield driver
    driver.quit()


def test_form(driver):
    form_page = FormPage(driver)
    form_page.open()
    form_page.fill_form()
    form_page.submit_form()
    form_page.check_form()
