from ..pages.profile_page import ProfilePage
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_delete_user(login):
    username = 'sele1@sele1.com'
    password = 'Ahoj12345'
    
    profile_page = ProfilePage(login)
    time.sleep(2)
    # profile_page.profile_button_click()
    profile_page.get("http://127.0.0.1:8000/user-profile")
    profile_page.edit_button_click()
    profile_page.delete_acc_button_click()
    profile_page.enter_password(password="Ahoj12345")
    profile_page.conf_delete_button_click()
    
    
    expected_url = profile_page.expected_delete_acc_url
    assert profile_page.driver.current_url == expected_url