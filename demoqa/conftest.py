# conftest.py
import pytest
from selenium import webdriver
from selene import Browser, Config
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    options = Options()

    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser = Browser(Config(driver))
    yield browser

