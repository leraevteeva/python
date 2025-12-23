from selenium import webdriver
from pages.login_page import LoginPage
from pages.shop_main_page import ShopMainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shop_total():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    shop = ShopMainPage(driver)
    shop.add_product("Sauce Labs Backpack")
    shop.add_product("Sauce Labs Bolt T-Shirt")
    shop.add_product("Sauce Labs Onesie")
    shop.open_cart()

    cart = CartPage(driver)
    cart.checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_form("Lera", "Test", "12345")

    total = checkout.get_total()

    driver.quit()

    assert total == "Total: $58.29"
