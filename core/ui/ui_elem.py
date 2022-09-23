import allure
from selene import factory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UiElem:
    default_timeout = 0

    def __init__(self, locator):
        self.locator = locator
        self.default_timeout = 30

    def get_wait(self, timeout_sec):
        dr = factory.get_shared_driver()

        print("Get driver wait for locator = " + self.locator[1] + ", time = " + str(timeout_sec) + " sec")
        ms = timeout_sec * 1000

        wait = WebDriverWait(dr, ms)
        return wait

    def locator_presence(self, timeout_sec=None):
        if timeout_sec == None:
            timeout_sec = self.default_timeout

        wait = self.get_wait(timeout_sec)
        presence = wait.until(EC.presence_of_element_located(((self.locator))))
        return presence

    def click(self, timeout_sec=None):
        with allure.step("click on -> " + str(self.locator)):
            if timeout_sec == None:
                timeout_sec = self.default_timeout
        wait = self.get_wait(timeout_sec)
        wait.until(EC.element_to_be_clickable((self.locator))).click()

    def type(self, text, timeout_sec=None):
        with allure.step("type text -> " + text + " to " + str(self.locator)):
            if timeout_sec == None:
                timeout_sec = self.default_timeout
        wait = self.get_wait(timeout_sec)
        wait.until(EC.element_to_be_clickable((self.locator))).send_keys(text)

    def find_elem(self, timeout_sec=None):
        if timeout_sec == None:
            timeout_sec = self.default_timeout
        wait = self.get_wait(timeout_sec)
        return wait.until(EC.visibility_of_element_located((self.locator)))

    def get_attr(self, attribute, timeout_sec=None):
        with allure.step("get attribute -> " + str(self.locator)):
            if timeout_sec == None:
                timeout_sec = self.default_timeout
        elem = self.find_elem(timeout_sec)
        return elem.get_attribute(attribute)
