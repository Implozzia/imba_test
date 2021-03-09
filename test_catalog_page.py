from .pages.catalog_page import CatalogPage
import time
import pytest


def test_order_from_catalog_page(browser):
    link = 'https://imba.shop/collection/tovary'
    page = CatalogPage(browser, link)
    browser.implicitly_wait(5)
    page.open()
    page.go_to_merch_tab()
    page.scroll_to_mousepad()
    page.add_mousepad_to_cart()
    page.use_promocode()
    page.should_be_promocode_text()
    page.go_to_order_page()
    page.fill_order_page_data()
    page.should_be_available_all_delivery()
    page.accept_order()
    time.sleep(10)