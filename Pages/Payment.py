from selenium.webdriver.common.by import By
import time
from Config.Config import TestData
from Pages.Basepage import BasePage

class Payment(BasePage):
    """By_locators== Object repository"""
    OWNER_NAME = (By.ID, "owner")
    CVV = (By.XPATH, "//input[@id='cvv']")
    CARD_NAME = (By.ID, "cardNumber")
    EXPIRY_MONTH = (By.ID, "expiration-month")
    EXPIRY_YEAR = (By.ID, "expiration-year")
    CONFIRM_PAYMENT = (By.ID, "confirm-purchase")
    COMPARE_PAYMENT_MESSAGE = (By.XPATH, "//h1[.='payment-complete']")

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def payment(self):
        self.do_send_keys(self.CVV, "123")
        self.do_send_keys(self.CARD_NAME, "4111111111111111")
        self.do_click(self.CONFIRM_PAYMENT)
