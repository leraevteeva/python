from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop_total_price():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    products = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie",
    ]

    for product in products:
        driver.find_element(By.ID, product).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Валерия")
    driver.find_element(By.ID, "last-name").send_keys("Евтеева")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    driver.find_element(By.ID, "continue").click()

    total = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    ).text

    driver.quit()

    assert total == "Total: $58.29"
