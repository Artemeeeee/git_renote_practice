# conftest.py
import pytest
from selenium import webdriver
from selene import Browser, Config, browser
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()

    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "127.0")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver


    yield browser
    browser.quit()
