import math

import allure
from selenium.common import (
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.BROWSER = browser
        self.BASE_URL = "https://selenium1py.pythonanywhere.com"
        self.WAIT = WebDriverWait(self.BROWSER, timeout=5)
        self.EC = ec

        self.LOGIN_LINK_LOCATOR = ("css selector", "#login_link")
        self.VIEW_BASKET_LINK_LOCATOR = ("css selector", ".basket-mini a")

        self.USER_ICON_LOCATOR = ("css selector", ".icon-user")

        self.PRODUCTS_CATALOGUE_URL = f"{self.BASE_URL}/catalogue"

    def open(self, url):
        self.BROWSER.get(url)

    def find_element(self, how, what):
        return self.BROWSER.find_element(how, what)

    @property
    def login_link(self):
        return self.find_element(*self.LOGIN_LINK_LOCATOR)

    def is_element_present(self, how, what):
        try:
            self.WAIT.until(self.EC.presence_of_element_located((how, what)))
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what):
        try:
            self.WAIT.until(self.EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    @allure.step("Assert page contains link to Login page")
    def should_be_login_link(self):
        assert self.is_element_present(
            *self.LOGIN_LINK_LOCATOR
        ), "Login link is not displayed, but should be"

    @allure.step("Click login link")
    def click_login_link(self):
        self.login_link.click()

    @property
    def view_basket_link(self):
        return self.find_element(*self.VIEW_BASKET_LINK_LOCATOR)

    @allure.step("Click View basket link")
    def click_view_basket_link(self):
        self.view_basket_link.click()

    @allure.step("Assert user icon is displayed")
    def should_be_authorized_user(self):
        assert self.is_element_present(
            *self.USER_ICON_LOCATOR
        ), "User icon is not displayed, probably unauthorised user"

    @allure.step("Solve quiz and send code in alert")
    def solve_quiz_and_send_code(self):
        alert = self.BROWSER.switch_to.alert
        number = alert.text.split("\n", 1)[0].split("=")[1].strip()
        answer = str(math.log(abs(12 * math.sin(float(number)))))

        alert.send_keys(answer)
        alert.accept()
