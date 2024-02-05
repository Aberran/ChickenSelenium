import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)
# options.add_argument("--headless")  # Enable headless mode
# options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

url_server = "https://chickenbook.pythonanywhere.com/"
url_localhost = "http://127.0.0.1:8000/"

@pytest.fixture(scope="function")
def driver():
    _driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    _driver.get(url_localhost)
    yield _driver
    # _driver.close()
    # _driver.quit()