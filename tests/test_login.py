from ..pages.login_page import LoginPage
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_log_in(driver):
    username = 'sele@sele.com'
    password = 'Ahoj12345'
    
    login_page = LoginPage(driver)
    login_page.visit_page()
    login_page.fill_name_input(username=username)
    login_page.fill_password_input(password=password)
    login_page.submit_form()
    
    expected_url = "http://127.0.0.1:8000/"
    assert driver.current_url == expected_url
    

    