from .pages.constructor_page import ConstructorPage
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest


def test_collect_pack(browser):
    link = 'https://imba.shop/page/combo-constructor'
    page = ConstructorPage(browser, link)
    browser.implicitly_wait(5)
    page.open()
    page.collect_pack()
