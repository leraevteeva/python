from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleMainPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.NAME, "q")
        self.results_block = (By.ID, "search")

    def search(self, query):
        search_input = self.driver.find_element(*self.search_input)
        search_input.clear()
        search_input.send_keys(query)
        search_input.send_keys(Keys.ENTER)

    def is_results_displayed(self):
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.results_block)
        )
        return True


