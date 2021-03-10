from .locators import CatalogPageLocators
from .locators import BasePageLocators
from .locators import CartPageLocators
from .locators import OrderPageLocators
from .base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
import time


class CatalogPage(BasePage):
    def go_to_merch_tab(self):
        merch_tab = self.browser.find_element(*CatalogPageLocators.MERCH_TAB)
        merch_tab.click()

    def scroll_to_mousepad(self):
        mousepad = self.browser.find_element(*CatalogPageLocators.SAMURAI_MOUSEPAD)
        ActionChains(self.browser).move_to_element(mousepad).perform()

    def add_mousepad_to_cart(self):
        mousepad_btn = self.browser.find_element(*CatalogPageLocators.SAMURAI_MOUSEPAD_BTN)
        mousepad_btn.click()
        cart_icon = self.browser.find_element(*BasePageLocators.CART_ICON)
        cart_icon.click()

    def use_promocode(self):
        promo_input = self.browser.find_element(*CartPageLocators.PROMO_INPUT)
        promo_input.send_keys('bebey')
        promo_btn = self.browser.find_element(*CartPageLocators.PROMO_BTN)
        promo_btn.click()

    def should_be_promocode_text(self):
        promo_text = self.browser.find_element(*CartPageLocators.PROMO_SUCCESS_TXT).text
        assert promo_text == 'Скидка по купону BEBEY', "Promocode text doesn't equal"

    def go_to_order_page(self):
        order_btn = self.browser.find_element(*CartPageLocators.ORDER_BTN)
        order_btn.click()

    def fill_order_page_data(self):
        number_input = self.browser.find_element(*OrderPageLocators.NUMBER)
        number_input.send_keys('+79110000000')

        name_input = self.browser.find_element(*OrderPageLocators.NAME)
        name_input.send_keys('test test')

        city_input = self.browser.find_element(*OrderPageLocators.CITY)
        city_input.clear()
        city_input.send_keys('г Нижний Новгород, Нижегородская обл.')
        name_input.click()

        address_input = self.browser.find_element(*OrderPageLocators.ADDRESS)
        address_input.send_keys('test test')

    def should_be_available_all_delivery(self):
        boxberry_offline = self.browser.find_element(*OrderPageLocators.BOXBERRY_OFFLINE).text
        assert boxberry_offline == 'Курьером Boxberry (Только онлайн оплата)', 'Boxberry courier is not available'
        boxberry_online = self.browser.find_element(*OrderPageLocators.BOXBERRY_ONLINE).text
        assert boxberry_online == 'Самовывоз Boxberry (Только онлайн оплата)', 'Boxberry pickup is not available'
        pickpoint = self.browser.find_element(*OrderPageLocators.PICKPOINT).text
        assert pickpoint == 'PickPoint (Только онлайн оплата)', 'Pickpoint is not available'
        via_delivery = self.browser.find_element(*OrderPageLocators.VIA_DELIVERY).text
        assert via_delivery == 'Via.Delivery – пункт выдачи рядом с домом', 'Via delivery is not available'

    def accept_order(self):
        news_checkbox = self.browser.find_element(*OrderPageLocators.NEWS_CHECKBOX)
        news_checkbox.click()
        order_btn = self.browser.find_element(*OrderPageLocators.CREATE_ORDER_BTN)
        order_btn.click()
