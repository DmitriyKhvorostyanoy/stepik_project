import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_bascet(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def should_be_correct_success_messages(self):
        self.should_be_correct_product_name_in_success_message()
        self.should_be_correct_price_in_success_message()

    def should_be_correct_product_name_in_success_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert product_name == added_product_name, 'Product name is different in the success message'

    def should_be_correct_price_in_success_message(self):
        product_price_str = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_in_success_message_str = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_SUCCESS_MESSAGE).text
        product_price = float(product_price_str[1:])
        price_in_success_message = float(price_in_success_message_str[1:])
        assert product_price==price_in_success_message,"Price is different in the success message"

