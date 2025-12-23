from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay = (By.ID, "delay")
        self.result = (By.CLASS_NAME, "screen")

    def set_delay(self, value):
        field = self.driver.find_element(*self.delay)
        field.clear()
        field.send_keys(value)

    def press(self, text):
        self.driver.find_element(By.XPATH, f"//span[text()='{text}']").click()

    def get_result(self):
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element(self.result, "15")
        )
        return self.driver.find_element(*self.result).text
