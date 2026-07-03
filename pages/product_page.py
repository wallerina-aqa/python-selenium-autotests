import allure

from pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.PRODUCT_NAME_LOCATOR = ("css selector", ".product_main h1")
        self.PRODUCT_PRICE_LOCATOR = ("css selector", ".product_main .price_color")

        self.ADD_TO_BASKET_BUTTON_LOCATOR = ("css selector", ".btn-add-to-basket")

        self.SUCCESS_ALERT_LOCATOR = (
            "css selector",
            ".alert-success:nth-child(1) .alertinner strong",
        )
        self.PRODUCT_PRICE_IN_SUCCESS_ALERT_LOCATOR = (
            "css selector",
            ".alert-info strong",
        )

    @allure.step("Open Product page")
    def open_product_page(self, link):
        self.open(link)

    @property
    def product_name(self):
        return self.find_element(*self.PRODUCT_NAME_LOCATOR).text

    @property
    def product_price(self):
        return self.find_element(*self.PRODUCT_PRICE_LOCATOR).text

    @property
    def add_to_basket_button(self):
        return self.find_element(*self.ADD_TO_BASKET_BUTTON_LOCATOR)

    @allure.step("Click Add to basket button")
    def click_add_to_basket_button(self):
        self.add_to_basket_button.click()

    @property
    def product_name_in_success_alert(self):
        return self.find_element(*self.SUCCESS_ALERT_LOCATOR).text

    @property
    def product_price_in_success_alert(self):
        return self.find_element(*self.PRODUCT_PRICE_IN_SUCCESS_ALERT_LOCATOR).text

    @allure.step("Assert success alert is displayed")
    def assert_success_alert(self):
        self.is_element_present(
            *self.SUCCESS_ALERT_LOCATOR
        ), "Success alert is not displayed, but should be"

    @allure.step("Assert success alert is not displayed")
    def assert_success_alert_absence(self):
        assert self.is_not_element_present(
            *self.SUCCESS_ALERT_LOCATOR
        ), "Success alert is displayed, but should not be"

    @allure.step("Check product name in successful alert")
    def assert_product_name_matches_original_product_name(self):
        assert self.product_name_in_success_alert == self.product_name, (
            f'Product name should be "{self.product_name}", '
            f'but product name in alert is "{self.product_name_in_success_alert}"'
        )

    @allure.step("Check product price in successful alert")
    def assert_product_price_matches_original_product_price(self):
        assert self.product_price_in_success_alert == self.product_price, (
            f'Basket price should be "{self.product_price}", '
            f'but basket price in alert is "{self.product_price_in_success_alert}"'
        )

    def assert_basket_messages(self):
        self.assert_success_alert()
        self.assert_product_name_matches_original_product_name()
        self.assert_product_price_matches_original_product_price()
