import time

from selenium.webdriver.common.by import By

base_url = "https://testautomationpractice.blogspot.com/"


class HomePageObject:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = "RESULT_TextField-1"

    def get_first_name(self):
        return self.driver.find_element(By.ID, self.first_name)

    def sign_up(self, first_name):
        self.get_first_name().send_keys(first_name)
        time.sleep(5)

    @staticmethod
    def get_base_url():
        return base_url
