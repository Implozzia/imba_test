from .pages.catalog_page import CatalogPage
from .pages.main_page import MainPage
from .pages.order_page import OrderPage
import time
import pytest


def test_order_from_catalog_page(browser):
    link = 'https://kz.imba.shop/'
    main_page = MainPage(browser, link)
    browser.implicitly_wait(5)
    main_page.open()
    main_page.add_to_basket_mosaic_item()
    main_page.popup_continue_shopping_btn()

