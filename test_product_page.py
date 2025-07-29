import time

from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser=browser, url=link)
    product_page.open()
    name_before_adding = product_page.get_product_name()
    price_before_adding = product_page.get_product_price()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()

    cart_page = CartPage(browser=browser, url=browser.current_url)
    name_after_adding = cart_page.get_product_name()
    price_after_adding = cart_page.get_product_price()

    cart_page.should_be_correct_price(price_before_adding, price_after_adding)
    cart_page.should_be_correct_product_name(name_before_adding, name_after_adding)

    time.sleep(10)