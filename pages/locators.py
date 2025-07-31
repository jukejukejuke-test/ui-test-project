from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BTN = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.ID, "id_registration-email")
    REGISTER_FORM_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_FORM_REPEAT_PASSWORD = (By.ID, "id_registration-password2")
    LOGIN_FORM_EMAIL = (By.ID, "id_login-username")
    LOGIN_FORM_PASSWORD = (By.ID, "id_login-password")
    REGISTER_BUTTON = (By.XPATH, "//*[@id='register_form']/button")

class ProductPageLocators:
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1][contains(@class, 'alert-success')]")

class CartPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-4>h3>a")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-1>.align-right")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1][contains(@class, 'alert-success')]")
    TEXT_ABOUT_EMPTY_CART = (By.CSS_SELECTOR, "#content_inner>p")