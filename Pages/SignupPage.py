from selenium.webdriver.common.by import By
import time
from Config.Config import TestData
from Pages.Basepage import BasePage

class SignupPage(BasePage):
    """By_locators== Object repository"""
    REGISTER =(By.XPATH, "//a[contains(text(), 'REGISTER')]")
    NAME=(By.ID,"name")
    EMAIL_ID=(By.ID, "email")
    PHONE_NUMBER=(By.ID, "phone")
    AGE = (By.XPATH, "// input[ @ name = 'age']")
    PASSWORD = (By.XPATH, "// input[ @ name = 'password']")
    CONFIRM_PASSWORD = (By.ID, "password-confirm")
    NEXT_BUTTON = (By.ID, "nextBtn")
    ADDRESS = (By.XPATH, "//input[@name='address']")
    CITY = (By.XPATH, "//input[@name='city']")
    ZIPCODE = (By.XPATH, "//input[@name='zipcode']")
    STATE = (By.XPATH, "//input[@name='state']")
    NEXT = (By.ID, "nextBtn")
    CHECKBOX1 = (By.XPATH, "//input[@value='Google']")
    CHECKBOX2 = (By.XPATH, "//input[@value='Bachelors']")
    TEXTFIELD1 = (By.XPATH, "//textarea[@name='biomagnetism_interest']")
    TEXTFIELD2 = (By.XPATH, "//textarea[@name='something_fun_to_know']")

    SIGNUP_CONFIRMATION = (By.XPATH, "//button[@type='button']/../strong")



    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)


    """This is used to login to app"""

    def do_signup(self, username, email, phoneno, age, password, confirmPassword):
        self.do_click(self.REGISTER)
        time.sleep(6)
        """page 1"""
        self.do_send_keys(self.NAME, username)
        self.do_send_keys(self.EMAIL_ID, email)
        self.do_send_keys(self.PHONE_NUMBER, phoneno)
        self.do_send_keys(self.AGE, age)
        self.do_send_keys(self.PASSWORD, password)
        self.do_send_keys(self.CONFIRM_PASSWORD, confirmPassword)
        time.sleep(6)
        self.do_click(self.NEXT_BUTTON)
        """page 2"""
        self.do_send_keys(self.ADDRESS, "BTM layout 2nd street")
        self.do_send_keys(self.CITY, "Bangalore")
        self.do_send_keys(self.ZIPCODE, "524002")
        self.do_send_keys(self.STATE, "Karnataka")
        time.sleep(6)
        self.do_click(self.NEXT)
        """page 3"""
        self.do_click(self.CHECKBOX1)
        self.do_click(self.CHECKBOX2)
        time.sleep(3)
        self.do_click(self.NEXT)
        self.do_send_keys(self.TEXTFIELD1, "Testing Purpose")
        self.do_send_keys(self.TEXTFIELD2, "Test")
        time.sleep(5)
        self.do_click(self.NEXT)



