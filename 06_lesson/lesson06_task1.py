from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

button = driver.find_element(By.ID, "ajaxButton")
button.click()

start = time()
green_text = None

while time() - start < 20:
    elements = driver.find_elements(By.CSS_SELECTOR, ".bg-success")
    if elements:
        green_text = elements[0]
        break

if green_text:
    print(green_text.text)
else:
    print("Зеленая плашка не появилась")

driver.quit()

