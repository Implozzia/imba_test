from selenium.webdriver.common.by import By


class BasePageLocators:
    ORDER_BTN = (By.CSS_SELECTOR, '.index-header__btn')


class ConstructorPageLocators:
    FIRST_ZIP = (By.CSS_SELECTOR, '.constructor__flex-item:nth-child(1)')
    SECOND_ZIP = (By.CSS_SELECTOR, '.constructor__flex-item:nth-child(2)')
    THIRD_ZIP = (By.CSS_SELECTOR, '.constructor__flex-item:nth-child(3)')
    FOURTH_ZIP = (By.CSS_SELECTOR, '.constructor__flex-item:nth-child(4)')
    SHAKER = (By.CSS_SELECTOR, '.constructor__flex-item:nth-child(5)')
    TASTE_BURATINO = (By.CSS_SELECTOR, '.constructor__taste-item:nth-child(1)')
    TASTE_ORIGINAL = (By.CSS_SELECTOR, '.constructor__taste-item:nth-child(2)')
    TASTE_POMEGRANATE = (By.CSS_SELECTOR, '.constructor__taste-item:nth-child(3)')
    TASTE_BELL_FLOWER = (By.CSS_SELECTOR, '.constructor__taste-item:nth-child(4)')
    SHAKER_FLASH = (By.CSS_SELECTOR, '.constructor__shaker-item:nth-child(3)')
    BTN_ADD_TO_CART = (By.CSS_SELECTOR, '.constructor__button--tocart')
    PROMO = (By.CSS_SELECTOR, '.cart-block__promo-text')


class BasketPageLocators:
    ORDER_BTN = (By.CSS_SELECTOR, '.cart-block__order-button')


class OrderPageLocators:
    NUMBER = (By.CSS_SELECTOR, '#client_phone')
    NAME = (By.CSS_SELECTOR, '#client_name')
    CITY = (By.CSS_SELECTOR, '#shipping_address_full_locality_name')
    ADDRESS = (By.CSS_SELECTOR, '#shipping_address_address')
    ORDER_BTN = (By.CSS_SELECTOR, '#create_order')