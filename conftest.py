import pytest
from selenium import webdriver
from selene import browser
import os


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")
    options.add_argument(f"--user-data-dir=/tmp/chrome_user_data_{os.getpid()}")

    browser.config.driver_options = options
    browser.config.driver_name = "chrome"
    browser.config.base_url = "https://github.com"
    browser.config.timeout = 10

    yield

    browser.quit()