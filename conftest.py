import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

@pytest.fixture(scope="function")
def driver():
    _driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    _driver.get("https://chickenbook.pythonanywhere.com/")
    yield _driver