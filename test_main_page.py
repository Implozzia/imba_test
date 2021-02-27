from .pages.main_page import MainPage
import time
import pytest


def test_order_btn_from_main_page(browser):
    link = 'https://imba.shop/'
    page = MainPage(browser, link)
    page.open()
    page.add_to_basket()
    time.sleep(10)
