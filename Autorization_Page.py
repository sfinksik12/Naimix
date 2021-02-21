import os

from BaseDefs.base import WebPage
from BaseDefs.elements import WebElement
from BaseDefs.elements import ManyWebElements
from selenium.webdriver.common.by import By


class Autorization(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url ='https://nm-test.mmtr.ru/login'

        super().__init__(web_driver, url)

    agree_and_close = WebElement(class_name=('login-cookie__button'))
    # Autorization prosess
    email = WebElement(name='login')
    password = WebElement(name='password')
    into_button = WebElement(xpath='//*[@id="root"]/div[2]/div[2]/div/div[1]/form/button')
    # Check into
    nmx_menu = WebElement(class_name='nmx-menu')

