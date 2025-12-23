from selenium import webdriver
from pages.calculator_page import CalculatorPage


def test_calculator():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    page = CalculatorPage(driver)

    page.set_delay(45)
    page.press("7")
    page.press("+")
    page.press("8")
    page.press("=")

    result = page.get_result()

    driver.quit()

    assert result == "15"
