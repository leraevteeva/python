from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.form_page import FormPage

def test_web_form():
    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/web-form.html")

    page = FormPage(driver)
    wait = WebDriverWait(driver, 10)

    # Заполняем поля
    page.fill_text_input("Иван")
    page.fill_password("пароль123")
    page.fill_textarea("Это тестовое сообщение")

    # Сабмит формы
    page.submit()

    # Проверка перехода на страницу с результатами
    assert "submitted-form.html" in driver.current_url

    driver.quit()
