from .locators import BasePageLocators
from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def add_to_basket(self):
        basket_btn = self.browser.find_element(*BasePageLocators.ORDER_BTN)
        basket_btn.click()

    def add_to_basket_mosaic_item(self):
        add_to_basket_btn = self.browser.find_element(*MainPageLocators.MOSAIC_ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def popup_continue_shopping_btn(self):
        popup_continue_shopping_btn = self.browser.find_element(*MainPageLocators.POPUP_CONTINUE_SHOPPING)
        popup_continue_shopping_btn.click()