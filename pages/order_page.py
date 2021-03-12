from .locators import OrderPageLocators
from .base_page import BasePage
import time


class OrderPage(BasePage):
    def iframe_order(self):
        time.sleep(5)
        self.browser.switch_to.frame(self.browser.find_element(*OrderPageLocators.IFRAME))
        card_btn = self.browser.find_element(*OrderPageLocators.ORDER_BTN_IFRAME)
        card_btn.click()



