from .locators import BasePageLocators
from .locators import ConstructorPageLocators
from .locators import BasketPageLocators
from .base_page import BasePage


class ConstructorPage(BasePage):
    def collect_pack(self):
        first_zip = self.browser.find_element(*ConstructorPageLocators.FIRST_ZIP)
        first_zip.click()
        select_first_zip = self.browser.find_element(*ConstructorPageLocators.TASTE_BURATINO)
        select_first_zip.click()

        second_zip = self.browser.find_element(*ConstructorPageLocators.SECOND_ZIP)
        second_zip.click()
        select_second_zip = self.browser.find_element(*ConstructorPageLocators.TASTE_ORIGINAL)
        select_second_zip.click()

        third_zip = self.browser.find_element(*ConstructorPageLocators.THIRD_ZIP)
        third_zip.click()
        select_third_zip = self.browser.find_element(*ConstructorPageLocators.TASTE_POMEGRANATE)
        select_third_zip.click()

        fourth_zip = self.browser.find_element(*ConstructorPageLocators.FOURTH_ZIP)
        fourth_zip.click()
        select_fourth_zip = self.browser.find_element(*ConstructorPageLocators.TASTE_BELL_FLOWER)
        select_fourth_zip.click()

        shaker = self.browser.find_element(*ConstructorPageLocators.SHAKER)
        shaker.click()
        select_shaker = self.browser.find_element(*ConstructorPageLocators.SHAKER_FLASH)
        select_shaker.click()

        add_to_cart_btn = self.browser.find_element(*ConstructorPageLocators.BTN_ADD_TO_CART)
        add_to_cart_btn.click()

    def should_be_combosale(self):
        combo_text = self.browser.find_element(*ConstructorPageLocators.PROMO).text
        assert combo_text == 'combosale1', 'Order without promocode'

