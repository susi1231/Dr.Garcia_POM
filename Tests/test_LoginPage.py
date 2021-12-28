import pytest

from Config.Config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Login(BaseTest):


    def test_login_page_title(self):
        self.loginpageObject = LoginPage(self.driver)
        title = self.loginpageObject.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginpageObject1 = LoginPage(self.driver)
        self.loginpageObject1.do_login(TestData.USER_NAME, TestData.PASSWORD)