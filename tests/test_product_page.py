import pytest
import random
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import CartPage


@pytest.mark.login
class TestLoginFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        login_page = LoginPage(browser=browser, url=link)
        login_page.open()
        email = f"{random.randint(1_000_000, 9_999_999)}@example.ru"
        password = "TestPassword!"
        login_page.register_new_user(email=email, password=password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser=browser, url=link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        product_page = ProductPage(browser=browser, url=link)
        product_page.open()
        name_before_adding = product_page.get_product_name()
        price_before_adding = product_page.get_product_price()
        product_page.add_to_cart()
        product_page.solve_quiz_and_get_code()
        product_page.go_to_cart()

        cart_page = CartPage(browser=browser, url=browser.current_url)
        name_after_adding = cart_page.get_product_name()
        price_after_adding = cart_page.get_product_price()

        cart_page.should_be_correct_price(price_before_adding, price_after_adding)
        cart_page.should_be_correct_product_name(name_before_adding, name_after_adding)



@pytest.mark.need_review
@pytest.mark.parametrize('page_id', ["0", "1", "2", "3", "4", "5", "6",
                                     pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, page_id):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{page_id}"
    product_page = ProductPage(browser=browser, url=link)
    product_page.open()
    name_before_adding = product_page.get_product_name()
    price_before_adding = product_page.get_product_price()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.go_to_cart()

    cart_page = CartPage(browser=browser, url=browser.current_url)
    name_after_adding = cart_page.get_product_name()
    price_after_adding = cart_page.get_product_price()

    cart_page.should_be_correct_price(price_before_adding, price_after_adding)
    cart_page.should_be_correct_product_name(name_before_adding, name_after_adding)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser=browser, url=link)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser=browser, url=link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser=browser, url=link)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()
    product_page.go_to_login_page()

    login_page = LoginPage(browser=browser, url=browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser=browser, url=link)
    product_page.open()
    product_page.go_to_cart()
    cart_page = CartPage(browser=browser, url=browser.current_url)
    cart_page.should_not_be_products()
