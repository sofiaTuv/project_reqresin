from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Базовая страница
    """

    def __init__(self, browser):
        self.browser = browser

    def wait_until(self, by, path):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((by, path)))
