from selenium.webdriver.common.by import By
import time
from Config.Config import TestData
from Pages.Basepage import BasePage

class LoginPage(BasePage):
     """By_locators== Object repository"""
     EMAIL=(By.ID, "email")
     PASSWORD=(By.ID, "password")
     LOGIN_BUTTON=(By.XPATH, "//button[contains(text(), 'Login')]")
     REGISTER_BUTTON=(By.LINK_TEXT, "REGISTER")

     """constructor of the page class"""
     def __init__(self, driver):
          super().__init__(driver)
          self.driver.get(TestData.BASE_URL)

     """page Actions"""
     """This is used to get the page title"""
     def get_login_page_title(self,title):
          return  self.get_title(title)

     """This is used to check signup link"""


     """This is used to login to app"""
     def do_login(self, username, password):
          self.do_send_keys(self.EMAIL, username)
          time.sleep(5)
          self.do_send_keys(self.PASSWORD, password)
          time.sleep(5)
          self.do_click(self.LOGIN_BUTTON)
          """return HomePage(self.driver)"""






