from selenium.webdriver.common.by import By
import time
from Config.Config import TestData
from Pages.Basepage import BasePage
from Pages.CoursePage import CoursePage
from Pages.LandingPage import LandingPage
from Pages.Payment import Payment


class Purchase_Knowledge_Course(BasePage):
    """By_locators== Object repository"""
    NAME = (By.XPATH, "//input[@id='InputName']")
    EMAIL = (By.XPATH, "//input[@id='InputEmail']")
    PHONE = (By.XPATH, "//input[@id='InputPhone']")
    COUNTRY = (By.XPATH, "//input[@id='InputCountry']")
    STATE = (By.XPATH, "//input[@id='InputState']")
    CITY = (By.XPATH, "//input[@id='InputCity']")
    ZIPCODE = (By.XPATH, "//input[@id='InputPincode']")
    PROMOCODE = (By.XPATH, "//input[@id='InputPromocode']")
    PROMOCODE = (By.XPATH, "//input[@id='InputPromocode']")
    APPLY_PROMOCODE = (By.XPATH, "//input[@id='InputApplypromocode']")
    CHECKBOX = (By.XPATH, "//input[@id='Check1']")
    BUYBUTTON = (By.XPATH, "//button[.='Buy the Course']")

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)


    def purchaseKnowledge_course(self):
        self.do_click(LandingPage.THREELINES)
        self.do_click(LandingPage.COURSE)
        self.do_click(CoursePage.KNOWLEDE_VIDEOS)
        self.do_send_keys(self.COUNTRY, "India")
        self.do_send_keys(self.STATE, "Karnataka")
        self.do_send_keys(self.CITY, "Bangalore")
        self.do_send_keys(self.ZIPCODE, "524002")
        self.do_click(self.CHECKBOX)
        self.do_click(self.BUYBUTTON)

