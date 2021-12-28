from selenium.webdriver.common.by import By
import time
from Config.Config import TestData
from Pages.Basepage import BasePage

class HomePage(BasePage):
     """By_locators== Object repository"""


     """constructor of the page class"""
     def __init__(self, driver):
          super().__init__(driver)
          self.driver.get(TestData.BASE_URL)