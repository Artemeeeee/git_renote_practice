# conftest.py
import pytest
from selenium import webdriver
from selene import Browser, Config
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
        "selenoid:options": {
            "enableVideo": True,
            "enableVNC": True

        }
    }

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser = Browser(Config(driver))
    yield browser
