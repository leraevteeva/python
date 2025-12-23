from selenium import webdriver
from pages.google_main_page import GoogleMainPage


def test_google_search():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/")

    page = GoogleMainPage(driver)
    page.search("Selenium Python")

    assert page.is_results_displayed()

    driver.quit()




