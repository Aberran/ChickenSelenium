from ..pages.login_page import LoginPage
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_log_in(driver):
    username = 'sele@sele.com'
    password = 'Ahoj12345'
    
    login_page = LoginPage(driver)
    login_page.login(username=username, password=password)

    
    expected_url = "http://127.0.0.1:8000/"
    assert driver.current_url == expected_url
    
    

    