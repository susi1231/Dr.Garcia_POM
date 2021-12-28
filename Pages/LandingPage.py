from selenium.webdriver.common.by import By
import time
from Config.Config import TestData
from Pages.Basepage import BasePage

class LandingPage(BasePage):
     """By_locators== Object repository"""
     USER_ICON = (By.XPATH, "//a[@id='dropdownMenuLink']/img")
     THREELINES = (By.XPATH, "//a[@class='nav-link page-scroll']/span")
     HEADERLOGO = (By.XPATH, "//a[@class='navbar-brand logo-image ml-5']/img")
     COURSE = (By.XPATH, "//a[.='COURSE']")
     ABOUTUS = (By.XPATH, "//a[.='ABOUT US']")
     FAQ = (By.XPATH, "//a[.='FAQ']")
     MEDIA = (By.XPATH, "//a[.='MEDIA / BLOGS']")
     CONTACT_US = (By.XPATH, "//a[.='CONTACT US']")
     FOOTER_LOGO = (By.XPATH, "(//img[@class='img-fluid'])[3]")
     SOCIAL_FACEBOOK = (By.XPATH, "//a[contains(@href,'facebook')]//i")
     SOCIAL_YOUTUBE = (By.XPATH, "//i[@class='fa fa-youtube-play']")
     NEWSLETTER = (By.XPATH, "//input[@name='email']")
     NEWSLETTER_SUBMIT = (By.XPATH, "//button[.='Submit']")
     NEWSLETTER_THANKSMESSAGE = (By.XPATH, "//span[contains(@class, 'subscribemessage')]/span")
     HELENZYS = (By.XPATH, "//a[contains(@href,'helenzys')]")
     RECENT_POST = (By.XPATH, "(// div[@class ='show-featured clearfix'] / div[2] // a)[1]")
     TERMS_CONDITIONS = (By.XPATH, "//a[.='Terms and Condition']")
     PRIVACYPOLICY = (By.XPATH, "//a[.='Privacy Policy']")


     """constructor of the page class"""
     def __init__(self, driver):
          super().__init__(driver)
          self.driver.get(TestData.BASE_URL)

     """page Actions"""
     """This is used to get the page title"""

     """
     def get_login_page_title(self, title):
          return self.get_title(title)
     """