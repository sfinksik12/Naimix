import os

from BaseDefs.base import WebPage
from BaseDefs.elements import WebElement
from BaseDefs.elements import ManyWebElements
from selenium.webdriver.common.by import By


class Main(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url ='https://nm-test.mmtr.ru/client'

        super().__init__(web_driver, url)

    nmx_menu = WebElement(class_name=('nmx-menu__settings'))

