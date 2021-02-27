from .locators import BasePageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def add_to_basket(self):
        basket_btn = self.browser.find_element(*BasePageLocators.ORDER_BTN)
        basket_btn.click()