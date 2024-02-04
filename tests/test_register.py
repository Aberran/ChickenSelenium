from ..pages.register_page import RegisterPage
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_register(driver):
    email = 'sele1@sele1.com'
    first_name = 'Janko'
    last_name = 'Hrasko'
    password_1 = 'Ahoj12345'
    password_2 = 'Ahoj12345'
    
    register_page = RegisterPage(driver)
    register_page.fill_email_input(email=email)
    register_page.fill_first_name_input(first_name=first_name)
    register_page.fill_last_name_input(last_name=last_name)
    register_page.fill_password1_input(password_1=password_1)
    register_page.fill_password2_input(password_2=password_2)
    
    # expected_url = "http://127.0.0.1:8000/"
    # assert driver.current_url == expected_url