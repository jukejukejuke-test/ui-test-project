from pages.base_page import BasePage
from pages.locators import CartPageLocators

class CartPage(BasePage):
    def get_product_name(self):
        return self.browser.find_element(*CartPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*CartPageLocators.PRODUCT_PRICE).text

    def should_be_correct_price(self, price_before_adding, price_after_adding):
        assert price_before_adding == price_after_adding, "Price was changed!"

    def should_be_correct_product_name(self, name_before_adding, name_after_adding):
        assert name_before_adding == name_after_adding, "Name of product was changed!"

    def should_not_be_success_message(self):
        assert self.is_not_element_appears(*CartPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_element_appears(*CartPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
