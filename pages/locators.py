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