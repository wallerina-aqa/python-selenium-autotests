import allure

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Open Main page")
    def open_main_page(self):
        self.open(self.BASE_URL)
