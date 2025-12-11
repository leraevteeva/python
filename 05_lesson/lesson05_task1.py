from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def main():
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/classattr")

    button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()

    driver.quit()


if __name__ == "__main__":
    main()


