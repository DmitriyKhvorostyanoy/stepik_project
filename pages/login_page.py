from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url,"Invalid URL"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not present"
        assert True

    def register_new_user(self,email, password):
        user_email = self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        user_pass = self.browser.find_element(*LoginPageLocators.REG_PASSWORD).send_keys(password)
        confirm_user_pass = self.browser.find_element(*LoginPageLocators.CONFIRM_REG_PASSWORD).send_keys(password)
        reg_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()