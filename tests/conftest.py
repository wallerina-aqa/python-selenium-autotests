from pathlib import Path

import pytest
from selenium import webdriver

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def pytest_configure(config):
    allure_dir = PROJECT_ROOT / "allure-results"
    allure_dir.mkdir(exist_ok=True)
    config.option.allure_report_dir = str(allure_dir)


def pytest_addoption(parser):
    # fmt: off
    parser.addoption("--language", action="store", default="en-gb",
         help="Choose language: ",
         choices=("ar", "ca", "cs", "da", "de", "en-gb", "el",
                  "es", "fi", "fr", "it", "ko", "nl", "pl",
                  "pt", "pt-br", "ro", "ru", "sk", "uk", "zh-hans")

         )
    # fmt: on


@pytest.fixture()
def browser(request):
    print("\nStart browser for test")

    driver_options = webdriver.ChromeOptions()

    driver_options.add_argument("--window-size=1920,1080")
    driver_options.add_argument("--headless=new")
    driver_options.add_argument("--disable-blink-features=AutomationControlled")
    driver_options.add_argument("--no-sandbox")
    driver_options.add_argument("--disable-dev-shm-usage")

    driver_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    user_language = request.config.getoption("--language")

    driver_options.add_experimental_option(
        "prefs",
        {
            "intl.accept_languages": user_language,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "autofill.profile_enabled": False,
            "autofill.credit_card_enabled": False,
        },
    )

    driver = webdriver.Chrome(options=driver_options)
    yield driver

    print("\nQuit browser")
    driver.quit()


@pytest.fixture()
def main_page(browser):
    return MainPage(browser)


@pytest.fixture()
def login_page(browser):
    return LoginPage(browser)


@pytest.fixture()
def product_page(browser):
    return ProductPage(browser)


@pytest.fixture()
def basket_page(browser):
    return BasketPage(browser)


@pytest.fixture()
def authorized_user(login_page):
    login_page.open_login_page()
    login_page.register_new_user()
    login_page.should_be_authorized_user()
