from Config.Config import TestData
from Pages.LoginPage import LoginPage
from Pages.SignupPage import SignupPage
from Tests.test_base import BaseTest

class Test_Signup(BaseTest):

    """
    def test_login_page_title(self):
        self.signup = SignupPage(self.driver)
        title = self.signup.get_title(TestData.SINUP_PAGE_TITLE)
        assert title == TestData.SIGNUP_PAGE_TITLE
    """

    def test_signup(self):
        self.signup = SignupPage(self.driver)
        self.signup.do_signup(TestData.NAME, TestData.SIGNUP_USER_EMAIL, TestData.PHONE_NUMBER, TestData.AGE, TestData.SIGNUP_PASSWORD, TestData.SIGNUP_CONFIRM_PASSWORD)
