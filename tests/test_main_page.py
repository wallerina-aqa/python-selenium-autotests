import allure
import pytest


@pytest.mark.main_page
@pytest.mark.regression
class TestMainPage:
    @allure.feature("Main page")
    @allure.story("Login from Main page")
    @allure.title("Guest should see login link on Main page")
    @pytest.mark.login
    @pytest.mark.guest
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, main_page):
        main_page.open_main_page()
        main_page.should_be_login_link()

    @allure.feature("Main page")
    @allure.story("Login from Main page")
    @allure.title("Guest can go to Login page from Main page")
    @pytest.mark.login
    @pytest.mark.guest
    @pytest.mark.smoke
    def test_guest_can_go_to_login_page(self, main_page, login_page):
        main_page.open_main_page()
        main_page.click_login_link()
        login_page.should_be_login_page()

    @allure.feature("Main page")
    @allure.story("Empty basket")
    @allure.title("Empty basket opened from Main page has no products")
    @pytest.mark.basket
    @pytest.mark.guest
    def test_guest_can_see_no_products_in_empty_basket_opened_from_main_page(
        self, main_page, basket_page
    ):
        main_page.open_main_page()
        main_page.click_view_basket_link()
        basket_page.assert_basket_has_no_products()
        basket_page.assert_basket_empty_message()
