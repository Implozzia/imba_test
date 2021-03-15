from selenium.webdriver.common.by import By


class BasePageLocators:
    ORDER_BTN = (By.CSS_SELECTOR, '.index-header__btn')
    CART_ICON = (By.CSS_SELECTOR, '.basket-link')


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
    BOXBERRY_OFFLINE = (By.XPATH, '//*[@id="delivery_variants"]/div[2]/div[1]/label[1]/span[2]/span[1]')
    BOXBERRY_ONLINE = (By.XPATH, '//*[@id="delivery_variants"]/div[2]/div[1]/label[2]/span[2]/span[1]')
    PICKPOINT = (By.XPATH, '//*[@id="delivery_variants"]/div[2]/div[1]/label[3]/span[2]/span[1]')
    VIA_DELIVERY = (By.CSS_SELECTOR, '#delivery_title_2860009')
    NEWS_CHECKBOX = (By.CSS_SELECTOR, '.co-input-information')
    CREATE_ORDER_BTN = (By.CSS_SELECTOR, '#create_order')
    DELIVERY_INFO = (By.CSS_SELECTOR, '.checkout-block__free-delivery')
    IFRAME = (By.CSS_SELECTOR, '.with-appled')
    ORDER_BTN_IFRAME = (By.XPATH, '//*[@id="paymentMethodsContainer"]/div[1]/button')
    CLOSE_ICON = (By.TAG_NAME, 'button')
    GOOGLE_BTN = (By.XPATH, '//*[@id="paymentMethodsContainer"]/div[2]/button-button')


class CatalogPageLocators:
    MERCH_TAB = (By.CSS_SELECTOR, '.productslist-categories__item--6')
    SAMURAI_MOUSEPAD = (By.CSS_SELECTOR, '.product-item:nth-child(7)')
    SAMURAI_MOUSEPAD_BTN = (By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/div[5]/button/div')


class CartPageLocators:
    PROMO_INPUT = (By.CSS_SELECTOR, '.cart-block__input-block')
    PROMO_BTN = (By.CSS_SELECTOR, '.cart-block__send-button')
    PROMO_SUCCESS_TXT = (By.CSS_SELECTOR, '.cart-block__promo-text')
    ORDER_BTN = (By.CSS_SELECTOR, '.cart-block__order-button')