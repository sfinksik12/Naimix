from Naimix.Naimix_Role.Admin_Naimix.Autorization_Page import Autorization
from Naimix.Naimix_Role.Admin_Naimix.MainPage import Main
from BaseDefs.base import *
import pytest
# python -m pytest -v --driver Chrome --driver-path chromedriver.exe


def test_Sing_in(web_browser):
    page = Autorization(web_browser)

    page.agree_and_close.click()
    page.password.is_clickable()

    page.email.send_keys('nmadmin')
    page.password.send_keys('nmadmin123')
    page.into_button.click()

    page.nmx_menu.is_visible()


