from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        cart_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        cart_btn.click()