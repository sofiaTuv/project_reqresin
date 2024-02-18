import pytest
from dotenv import load_dotenv
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()