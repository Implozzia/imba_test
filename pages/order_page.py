from .locators import OrderPageLocators
from .base_page import BasePage
from faker import Faker


class OrderPage(BasePage):
    def fill_order_form(self):
        fake = Faker()
        number = fake.phone_number()
        name = fake.name()
        city = fake.city()
        address = fake.address()

        number_input = self.browser.find_element(*OrderPageLocators.NUMBER)
        number_input.click()
        number_input.send_keys(number)

        name_input = self.browser.find_element(*OrderPageLocators.NAME)
        name_input.send_keys(name)

        city_input = self.browser.find_element(*OrderPageLocators.CITY)
        city_input.send_keys(city)

        address_input = self.browser.find_element(*OrderPageLocators.ADDRESS)
        address_input.send_keys(address)
