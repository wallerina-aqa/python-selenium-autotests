import allure
from faker import Faker

from pages.base_page import BasePage

faker = Faker()


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.URL_ENDPOINT = "accounts/login/"
        self.URL = self.BASE_URL + self.URL_ENDPOINT

        self.LOGIN_FORM_LOCATOR = ("css selector", "#login_form")
        self.REGISTER_FORM_LOCATOR = ("css selector", "#register_form")

        self.REGISTRATION_FORM_EMAIL_INPUT_LOCATOR = (
            "css selector",
            "#id_registration-email",
        )
        self.REGISTRATION_FORM_PASSWORD_INPUT_LOCATOR = (
            "css selector",
            "#id_registration-password1",
        )
        self.REGISTRATION_FORM_CONFIRM_PASSWORD_INPUT_LOCATOR = (
            "css selector",
            "#id_registration-password2",
        )
        self.SUBMIT_REGISTRATION_BUTTON_LOCATOR = (
            "css selector",
            "[name='registration_submit']",
        )
        self.THANKS_FOR_REGISTRATION_ALERT_LOCATOR = (
            "css selector",
            ".alert-success",
        )

    @allure.step("Open Login page")
    def open_login_page(self):
        self.open(self.URL)

    @allure.step("Assert Login page url")
    def should_be_login_url(self):
        assert self.BROWSER.current_url.endswith(self.URL_ENDPOINT), (
            f'Page url should end with "{self.URL_ENDPOINT}", '
            f'but actual url is "{self.BROWSER.current_url}"'
        )

    @allure.step("Assert page contains login form")
    def should_be_login_form(self):
        assert self.is_element_present(
            *self.LOGIN_FORM_LOCATOR
        ), "Login form is missing"

    @allure.step("Assert page contains register form")
    def should_be_register_form(self):
        assert self.is_element_present(
            *self.REGISTER_FORM_LOCATOR
        ), "Register form is missing"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    @property
    def registration_form_email_input(self):
        return self.find_element(*self.REGISTRATION_FORM_EMAIL_INPUT_LOCATOR)

    @property
    def registration_form_password_input(self):
        return self.find_element(*self.REGISTRATION_FORM_PASSWORD_INPUT_LOCATOR)

    @property
    def registration_form_confirm_password_input(self):
        return self.find_element(*self.REGISTRATION_FORM_CONFIRM_PASSWORD_INPUT_LOCATOR)

    @property
    def submit_registration_button(self):
        return self.find_element(*self.SUBMIT_REGISTRATION_BUTTON_LOCATOR)

    @allure.step("Register new user")
    def register_new_user(self):
        new_user_email = faker.email()
        new_user_password = faker.password()

        self.registration_form_email_input.send_keys(new_user_email)
        self.registration_form_password_input.send_keys(new_user_password)
        self.registration_form_confirm_password_input.send_keys(new_user_password)
        self.submit_registration_button.click()

        self.is_element_present(*self.THANKS_FOR_REGISTRATION_ALERT_LOCATOR), (
            "Thanks for registration alert should be displayed, "
            "but it is not present"
        )
