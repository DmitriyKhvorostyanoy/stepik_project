from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR,"#register_form")
    REG_EMAIL= (By.CSS_SELECTOR,"#id_registration-email")
    REG_PASSWORD= (By.CSS_SELECTOR,"#id_registration-password1")
    CONFIRM_REG_PASSWORD = (By.CSS_SELECTOR,"#id_registration-password2")
    REGISTER_BUTTON =  (By.CSS_SELECTOR,"[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR,"#add_to_basket_form>[type='submit']")
    PRODUCT_NAME = (By.CSS_SELECTOR,'.product_main>h1')
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR,"#messages div:first-child strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_page .price_color')
    PRODUCT_PRICE_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:last-of-type strong')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR,".btn-group > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASKET_NOTICE = (By.CSS_SELECTOR,'#content_inner > p')
    BASKET_ITEMS = (By.CSS_SELECTOR,'.basket-items')