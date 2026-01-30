from selenium.webdriver.chrome.options import Options


class Browser:
    def __init__(self):
        # Настройки Chrome для полноэкранного режима
        chrome_options = Options()
        chrome_options.add_argument("--start-fullscreen")

    def open(self, url):
        self.driver.get(url)