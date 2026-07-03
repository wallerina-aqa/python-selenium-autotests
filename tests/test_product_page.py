import allure
import pytest


@pytest.mark.product_page
@pytest.mark.regression
class TestProductPage:
    @allure.feature("Product page")
    @allure.story("Login from Product page")
    @allure.title("Guest should see login link on Product page")
    @pytest.mark.guest
    @pytest.mark.smoke
    def test_guest_should_see_login_link_on_product_page(self, product_page):
        link = product_page.PRODUCTS_CATALOGUE_URL + "/the-city-and-the-stars_95"
        product_page.open_product_page(link)
        product_page.should_be_login_link()

    @allure.feature("Product page")
    @allure.story("Login from Product page")
    @allure.title("Guest can go to Login page from Product page")
    @pytest.mark.guest
    @pytest.mark.smoke
    def test_guest_can_go_to_login_page_from_product_page(
        self, product_page, login_page
    ):
        link = product_page.PRODUCTS_CATALOGUE_URL + "/test-driven-development_124"
        product_page.open_product_page(link)
        product_page.click_login_link()
        login_page.should_be_login_page()

    @allure.feature("Product page")
    @allure.story("Adding product to basket")
    @allure.title("Guest can add product to basket")
    @pytest.mark.basket
    @pytest.mark.guest
    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "num",
        # fmt: off
        [
            0, 1, 2, 3, 4, 5, 6,
            pytest.param(7, marks=pytest.mark.xfail),
            8, 9
        ],
        # fmt: on
    )
    def test_guest_can_add_product_to_basket(self, num, product_page):
        link = (
            product_page.PRODUCTS_CATALOGUE_URL
            + f"/coders-at-work_207/?promo=offer{num}"
        )
        product_page.open_product_page(link)
        product_page.click_add_to_basket_button()
        product_page.solve_quiz_and_send_code()
        product_page.assert_basket_messages()

    @allure.feature("Product page")
    @allure.story("Adding product to basket")
    @allure.title("Authorized user can add product to basket")
    @pytest.mark.basket
    @pytest.mark.user
    @pytest.mark.smoke
    def test_user_can_add_product_to_basket(self, authorized_user, product_page):
        link = product_page.PRODUCTS_CATALOGUE_URL + "/coders-at-work_207"
        product_page.open_product_page(link)
        product_page.click_add_to_basket_button()
        product_page.assert_basket_messages()

    @allure.feature("Product page")
    @allure.story("Adding product to basket")
    @allure.title("Guest see no messages on Product page")
    @pytest.mark.basket
    @pytest.mark.guest
    def test_guest_should_not_see_success_basket_message(self, product_page):
        link = product_page.PRODUCTS_CATALOGUE_URL + "/the-clean-coder_150"
        product_page.open_product_page(link)
        product_page.assert_success_alert_absence()

    @allure.feature("Product page")
    @allure.story("Adding product to basket")
    @allure.title("Authorized user see no messages on Product page")
    @pytest.mark.basket
    @pytest.mark.user
    def test_user_should_not_see_success_basket_message(
        self, authorized_user, product_page
    ):
        link = product_page.PRODUCTS_CATALOGUE_URL + "/the-clean-coder_150"
        product_page.open_product_page(link)
        product_page.assert_success_alert_absence()

    @allure.feature("Product page")
    @allure.story("Empty basket")
    @allure.title("Empty basket opened from Product page has no products")
    @pytest.mark.basket
    @pytest.mark.guest
    def test_guest_can_see_no_products_in_empty_basket_opened_from_product_page(
        self, product_page, basket_page
    ):
        link = (
            product_page.PRODUCTS_CATALOGUE_URL
            + "/sams-teach-yourself-mysql-in-24-hours_145"
        )
        product_page.open_product_page(link)
        product_page.click_view_basket_link()
        basket_page.assert_basket_has_no_products()
        basket_page.assert_basket_empty_message()
