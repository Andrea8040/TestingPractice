import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.actions_chains import ActionChains

base_url = "https://testautomationpractice.blogspot.com/"

class HomePageObject:

    def __init__(self, driver):
        self.driver = driver
        self.form_name = "name"
        self.form_email = "email"
        self.form_phone = "phone"
        self.form_address = "textarea"
        self.genderRadioButton = "male"
        self.dayRadioButton = "saturday"
        self.countryDropDownList = "country"
        self.colorList = "colors"
        self.calendar = "datepicker"
        self.fotterPagination = "pagination"
        #self.checkProductTable = "productTable"
        self.wikipedia_search = "Wikipedia1_wikipedia-search-input"
        self.search_button = "wikipedia-search-button"
        self.browser_windows_button = "//button[@onclick='myFunction()']"
        self.alert_Button = "xpath=//button[@onclick='myFunctionAlert()']"
        self.double_Click = "css=button:nth-child(6)"
        self.draggable_Position = "draggable"
        self.dropeable_Position = "dropeable"

    def get_first_name(self):
        return self.driver.find_element(By.ID, self.form_name)

    def get_form_email(self):
        return self.driver.find_element(By.ID, self.form_email)

    def get_form_phone(self):
        return self.driver.find_element(By.ID, self.form_phone)

    def get_form_address(self):
        return self.driver.find_element(By.ID, self.form_address)

    def get_gender_radio_button(self):
        return self.driver.find_element(By.ID, self.genderRadioButton)

    def get_select_day_radio_button(self):
        return self.driver.find_element(By.ID, self.dayRadioButton)

    def get_country_drop_down_list(self):
        return self.driver.find_element(By.ID, self.countryDropDownList)

    def get_check_genders(self):
        return self.driver.find_element(By.ID, self.genderRadioButton)

    def get_color_list(self):
        return self.driver.find_element(By.ID, self.colorList)

    def get_calendar(self):
        return self.driver.find_element(By.ID, self.calendar)

    def get_Fotter_Pagination(self):
        return self.driver.find_element(By.ID, self.fotterPagination)

    #def get_Check_Product_Table(self):
        #return self.driver.find_element(By.ID, self.checkProductTable)

    def get_wikipedia_search(self):
        return self.driver.find_element(By.ID, self.wikipedia_search)

    def get_search_button(self):
        return self.driver.find_element(By.CLASS_NAME, self.search_button)

    def get_browser_windows(self):
        return self.driver.find_element(By.XPATH, self.browser_windows_button)

    def get_alert_Button(self):
        return self.driver.find_element(By.XPATH, self.alert_Button)

    def get_draggable_Position(self):
        return self.driver.find_element(By.ID, self.draggable_Position)

    def get_dropeable_Position(self):
        return self.driver.find_element(By.ID, self.dropeable_Position)

    #def get_Double_Click(self):
     #   return self.driver.find_element(By.CLASS_NAME, self.double_Click)

    def sign_up(self, form_name, form_mail, form_phone, form_address, calendar, wikipedia_search):
        self.get_first_name().send_keys(form_name)
        self.get_form_email().send_keys(form_mail)
        self.get_form_phone().send_keys(form_phone)
        self.get_form_address().send_keys(form_address)
        time.sleep(2)

        self.scroll_page(self.get_gender_radio_button())
        self.get_select_day_radio_button().click()
        self.get_country_drop_down_list().click()

        # Select drop down list element
        time.sleep(2)
        select = Select(self.get_country_drop_down_list())
        select.select_by_visible_text('France')
        self.scroll_page(self.get_color_list())

        # Scroll Down
        select = Select(self.get_color_list())
        select.select_by_visible_text('White')
        self.get_calendar().send_keys(calendar)
        time.sleep(2)
        self.scroll_page(self.get_Fotter_Pagination())
        time.sleep(2)
        #self.scroll_page(self.get_wikipedia_search())
        self.get_wikipedia_search().send_keys(wikipedia_search)
        time.sleep(2)
        self.get_search_button().click()
        self.get_browser_windows().click()
        #self.get_check_genders().click()
        self.get_alert_Button().click()
        time.sleep(3)
        self.scroll_page(self.get_form_address())
        #self.get_Double_Click().double_click()




    @staticmethod
    def get_base_url():
        return base_url

    def scroll_page(self, target_element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", target_element)
        target_element.click()
