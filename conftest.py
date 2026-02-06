# conftest.py
import pytest


from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.options import Options
from utils import attach


DEFAULT_BROWSER_VERSION = '127.0'
def pytest_addoption(parser):
    parser.addoption(
        "--browser_version",
        default="127.0"
    )


@pytest.fixture(scope='function')
def setup_browser(request):
    browser_version = request.config.getoption("--browser_version")
    browser_version = browser_version if browser_version != '' else DEFAULT_BROWSER_VERSION
    options = Options()

    options.set_capability("browserName", 'chrome')
    options.set_capability("browserVersion", browser_version)
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver


    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)


    browser.quit()
