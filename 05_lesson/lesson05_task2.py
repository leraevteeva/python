from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/dynamicid")

    button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

    driver.quit()


if __name__ == "__main__":
    main()
