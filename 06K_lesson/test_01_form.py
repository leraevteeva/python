from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    wait.until(
        EC.presence_of_element_located((By.NAME, "first-name"))
    ).send_keys("Иван")

    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys(
        "test@skypro.com"
    )
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    submit_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView(true);", submit_button
    )
    submit_button.click()

    zip_code = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )

    assert "alert-danger" in zip_code.get_attribute("class")

    green_fields = driver.find_elements(By.CLASS_NAME, "alert-success")
    assert len(green_fields) == 9

    driver.quit()
