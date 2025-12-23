from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_field(self, locator, value):
        field = self.wait.until(EC.presence_of_element_located(locator))
        field.clear()
        field.send_keys(value)

    # Методы для конкретных полей формы
    def fill_text_input(self, value):
        self.fill_field((By.NAME, "my-text"), value)

    def fill_password(self, value):
        self.fill_field((By.NAME, "my-password"), value)

    def fill_textarea(self, value):
        self.fill_field((By.NAME, "my-textarea"), value)

    def submit(self):
        button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))
        )
        # Скроллим кнопку в видимую область
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        # Ждём кликабельности
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        button.click()
