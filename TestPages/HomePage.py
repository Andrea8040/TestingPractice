import time

from TestBase.WebDriverSetup import WebDriverSetup
from PageObject.HomeObject import HomePageObject


class Test_course_pack(WebDriverSetup):

    def test_add_form_element(self):
        driver = self.driver
        self.driver.get(HomePageObject.get_base_url())
        home_object = HomePageObject(driver)
        time.sleep(3)
        home_object.sign_up("daniel")

