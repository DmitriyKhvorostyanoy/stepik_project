from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_displayed_that_basket_is_empty()
        self.should_be_no_products_in_basket()

    def should_be_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
        "Basket contains products"

    def should_be_displayed_that_basket_is_empty(self):
        basket_empty_notice = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_NOTICE).text
        assert "Your basket is empty" in basket_empty_notice, "basket is not empty"
