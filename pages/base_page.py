from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.maximize_window()

    def open(self):
        self.browser.get(self.url)

