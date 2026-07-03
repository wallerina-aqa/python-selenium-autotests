import allure

from pages.base_page import BasePage


class BasketPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.PRODUCTS_IN_BASKET_LOCATOR = ("css selector", "#basket_formset")
        self.EMPTY_BASKET_MESSAGE_LOCATOR = ("css selector", "#content_inner p")

    @allure.step("Assert basket has no products")
    def assert_basket_has_no_products(self):
        self.is_not_element_present(
            *self.PRODUCTS_IN_BASKET_LOCATOR
        ), "There should be no products in basket, but it contains some"

    @allure.step("Assert basket has message that it is empty")
    def assert_basket_empty_message(self):
        self.is_element_present(
            *self.EMPTY_BASKET_MESSAGE_LOCATOR
        ), "Empty basket message is not displayed, but should be"
