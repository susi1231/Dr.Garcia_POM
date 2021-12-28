import pytest
import time
from Config.Config import TestData
from Pages.CoursePage import CoursePage
from Pages.LandingPage import LandingPage
from Pages.Payment import Payment
from Pages.PurchaseMainCourse import Purchase_Main_Course
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_PurchaseMainCourse(BaseTest):


    def test_purseMaincourse(self):
        self.loginpageObject1 = LoginPage(self.driver)
        self.main = Purchase_Main_Course(self.driver)
        self.paymentObject = Payment(self.driver)
        self.loginpageObject1.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.main.purchase_course()
        time.sleep(4)
        self.paymentObject.payment()
