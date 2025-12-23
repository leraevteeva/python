from selenium.webdriver.common.by import By


class ShopMainPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product(self, name):
        self.driver.find_element(
            By.XPATH, f"//div[text()='{name}']/ancestor::div[@class='inventory_item']//button"
        ).click()

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
