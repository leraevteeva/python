from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

start = time()
images = []
while time() - start < 20:
    images = driver.find_elements(By.CSS_SELECTOR, "img")
    if images and all(img.get_attribute("src") for img in images):
        break

if len(images) >= 3:
    third_image_src = images[2].get_attribute("src")
    print(third_image_src)
else:
    print("На странице меньше 3 загруженных картинок")

driver.quit()



