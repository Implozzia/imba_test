from .pages.catalog_page import CatalogPage
from .pages.locators import CatalogPageLocators
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest


def test_order_from_catalog_page(browser):
    link = 'https://imba.shop/collection/tovary'
    page = CatalogPage(browser, link)
    page.open()
    merch_tab = browser.find_element(*CatalogPageLocators.MERCH_TAB)
    merch_tab.click()
    mousetab = browser.find_element(*CatalogPageLocators.SAMURAI_MOUSEPAD)
    actions = ActionChains(browser)
    actions.move_to_element(mousetab).perform()
    time.sleep(10)

