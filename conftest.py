import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from .pages.login_page import LoginPage

url_localhost = "http://127.0.0.1:8000/"

options = Options()
options.add_experimental_option("detach", True)
# options.add_argument("--headless")  # Enable headless mode
# options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

@pytest.fixture(scope="function")
def driver():
    _driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    _driver.implicitly_wait(10)
    yield _driver
    _driver.close()
    _driver.quit()

@pytest.fixture
def login(driver):
    driver.get(url_localhost + "login/")
    login_page = LoginPage(driver)
    login_page.login("sele1@sele1.com", "Ahoj12345")
    return driver