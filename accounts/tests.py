import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException


# --------------------------------------------------------------------
#                       REGISTRATION TEST CASES
# --------------------------------------------------------------------
class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/Chris/Documents/Coding_Environments/chromedriver")
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("http://localhost:8000/signup/")
        driver.find_element_by_id("first_name").click()
        driver.find_element_by_id("first_name").clear()
        driver.find_element_by_id("first_name").send_keys("chris")
        driver.find_element_by_id("last_name").clear()
        driver.find_element_by_id("last_name").send_keys("homer")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("chris_homer93@hotmail.com")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("chris9772")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("chris_homer93@hotmail.com")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Hi, welcome to TextLeak!'])[1]/following::div[2]").click()
        driver.find_element_by_id("confirm_Password").click()
        driver.find_element_by_id("confirm_Password").clear()
        driver.find_element_by_id("confirm_Password").send_keys("hello123")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("hello123")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Please fill in your details below:'])[1]/following::input[7]").click()
        driver.find_element_by_id("first_name").click()
        driver.find_element_by_id("first_name").clear()
        driver.find_element_by_id("first_name").send_keys(
            "sdjfhsdfhdsjkfhskjfdhsjdhfdjkshfsdfjkdkshfkjdshfskfhdsjfhdkjds")
        driver.find_element_by_id("last_name").clear()
        driver.find_element_by_id("last_name").send_keys("sdfjkdsjfks")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("sdkjfksj")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("hello@email.com")
        driver.find_element_by_id("confirm_Password").clear()
        driver.find_element_by_id("confirm_Password").send_keys("hello123")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("hello123")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Please fill in your details below:'])[1]/following::input[7]").click()
        driver.find_element_by_id("first_name").click()
        driver.find_element_by_id("first_name").clear()
        driver.find_element_by_id("first_name").send_keys("jhfsdjfhs")
        driver.find_element_by_id("last_name").clear()
        driver.find_element_by_id("last_name").send_keys("sjdfhjshs")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("sdjfjdshf")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("sdfkhfs@kfdjsk")
        driver.find_element_by_id("confirm_Password").clear()
        driver.find_element_by_id("confirm_Password").send_keys("sdhfdsj")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("sdjfhsjh")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Please fill in your details below:'])[1]/following::input[7]").click()
        driver.find_element_by_id("first_name").click()
        driver.find_element_by_id("first_name").clear()
        driver.find_element_by_id("first_name").send_keys("james")
        driver.find_element_by_id("last_name").clear()
        driver.find_element_by_id("last_name").send_keys("nichol")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("james")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("james789@email.com")
        driver.find_element_by_id("confirm_Password").clear()
        driver.find_element_by_id("confirm_Password").send_keys("hello")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("hello")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Please fill in your details below:'])[1]/following::input[7]").click()
        driver.find_element_by_id("first_name").click()
        driver.find_element_by_id("first_name").clear()
        driver.find_element_by_id("first_name").send_keys("james")
        driver.find_element_by_id("last_name").clear()
        driver.find_element_by_id("last_name").send_keys("nichol")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("james")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("james123@email.com")
        driver.find_element_by_id("confirm_Password").clear()
        driver.find_element_by_id("confirm_Password").send_keys("hello123")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("hello123")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Please fill in your details below:'])[1]/following::input[7]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()


# --------------------------------------------------------------------
#                       LOGIN TEST CASES
# --------------------------------------------------------------------
class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/Chris/Documents/Coding_Environments/chromedriver")
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("http://localhost:8000/")
        driver.find_element_by_id("button").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Home'])[1]/following::fieldset[1]").click()
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("test123")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("skdjfks")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Please Sign In'])[1]/following::input[3]").click()
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("mark123")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("skdjfks")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Please Sign In'])[1]/following::input[3]").click()
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("MARK123")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("hello123")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Please Sign In'])[1]/following::input[3]").click()
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("mark123")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("hello123")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Please Sign In'])[1]/following::input[3]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
