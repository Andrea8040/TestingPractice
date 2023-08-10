import time
from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By

base_url = "https://testautomationpractice.blogspot.com/"


class HomePageObject:

    def __init__(self, driver):
        self.driver = driver
        self.form_name = "name"
        self.form_email = "email"
        self.form_phone = "phone"
        self.form_address = "textarea"
        self.check_gender = "male"

    def get_first_name(self):
        return self.driver.find_element(By.ID, self.form_name)

    def get_form_email(self):
        return self.driver.find_element(By.ID, self.form_email)

    def get_form_phone(self):
        return self.driver.find_element(By.ID, self.form_phone)

    def get_form_address(self):
        return self.driver.find_element(By.ID, self.form_address)

    #def get_scroll_down(self):
     #   flag = driver.find_element(By.ID, self.form_address)
      #  driver.execute_script("arguments(0).scrollIntoView();",flag)

    #def get_check_gender(self):
     #   return self.driver.find_element(By.ID, self.check_gender)

    def sign_up(self, form_name, form_mail, form_phone, form_address):
        self.get_first_name().send_keys(form_name)
        self.get_form_email().send_keys(form_mail)
        self.get_form_phone().send_keys(form_phone)
        self.get_form_address().send_keys(form_address)
        time.sleep(2)
        #self.get_check_gender().click()

    #def form_check(self):
     #   self.get_check_gender().click()

    @staticmethod
    def get_base_url():
        return base_url
