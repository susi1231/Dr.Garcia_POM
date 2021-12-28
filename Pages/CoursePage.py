from selenium.webdriver.common.by import By
import time
from Config.Config import TestData
from Pages.Basepage import BasePage

class CoursePage(BasePage):
     """By_locators== Object repository"""
     APPLY_COURSE = (By.XPATH, "//button[.='Apply for Course ']")
     KNOWLEDE_VIDEOS = (By.XPATH, "(//input[@class='btn btn-primary uppercase buybutton'])[5]")


     """constructor of the page class"""
     def __init__(self, driver):
          super().__init__(driver)
          self.driver.get(TestData.BASE_URL)
