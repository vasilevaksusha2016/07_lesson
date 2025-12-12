from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(driver, 45)
        self.delay_input = "delay"
        self.screen = "div.screen"
        self.button_7 = "//span[text()='7']"
        self.button_plus = "//span[text()='+']"
        self.button_8 = "//span[text()='8']"
        self.button_equals = "//span[text()='=']"

    def open(self):
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
            )

    def entering_delay(self):
        element_delay = self._driver.find_element(By.ID, self.delay_input)
        element_delay.clear()
        element_delay.send_keys("45")

    def button_click(self):
        buttons = [self.button_7,
                   self.button_plus,
                   self.button_8,
                   self.button_equals
                   ]
        for button in buttons:
            self._driver.find_element(By.XPATH, button).click()

    def get_screen_text(self):
        return self._driver.find_element(By.CSS_SELECTOR, self.screen).text

    def wait_for_result(self, expected_text):
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, self.screen), expected_text))
