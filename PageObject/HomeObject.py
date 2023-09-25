import time

from selenium.webdriver.common.by import By

base_url = "https://testautomationpractice.blogspot.com/"


class HomePageObject:

    def __init__(self, driver):
        self.driver = driver
        self.form_name = "name"
        self.form_email = "email"
        self.form_phone = "phone"
        self.form_address = "textarea"
        self.wikipedia_search = "Wikipedia1_wikipedia-search-input"
        self.search_button = "wikipedia-search-button"
        self.browser_windows_button = "//button[@onclick='myFunction()']"


    def get_first_name(self):
        return self.driver.find_element(By.ID, self.form_name)

    def get_form_email(self):
        return self.driver.find_element(By.ID, self.form_email)

    def get_form_phone(self):
        return self.driver.find_element(By.ID, self.form_phone)

    def get_form_address(self):
        return self.driver.find_element(By.ID, self.form_address)

    def get_wikipedia_search(self):
        return self.driver.find_element(By.ID, self.wikipedia_search)

    def get_search_button(self):
        return self.driver.find_element(By.CLASS_NAME, self.search_button)

    def get_browser_windows(self):
        return self.driver.find_element(By.XPATH, self.browser_windows_button)

     #   flag = driver.find_element(By.ID, self.form_address)
      #  driver.execute_script("arguments(0).scrollIntoView();",flag)

    #def get_check_gender(self):

     #   return self.driver.find_element(By.ID, self.check_gender)

    def sign_up(self, form_name, form_mail, form_phone, form_address, wikipedia_search):
        self.get_first_name().send_keys(form_name)
        self.get_form_email().send_keys(form_mail)
        self.get_form_phone().send_keys(form_phone)
        self.get_form_address().send_keys(form_address)
        self.get_wikipedia_search().send_keys(wikipedia_search)
        self.get_search_button().click()
        time.sleep(2)
        self.get_browser_windows().click()
        #
        self.driver.execute_script("windows.scrollTo(0,document.body.scrollHeight)")

    #def form_check(self):
     #   self.get_check_gender().click()

    @staticmethod
    def get_base_url():
        return base_url
