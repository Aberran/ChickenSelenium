from ..pages.profile_page import ProfilePage
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_delete_user(login):
    
    profile_p = ProfilePage(login)
    profile_p.visit_profile_page()
    time.sleep(2)
    profile_p.edit_button_click()
    profile_p.delete_acc_button_click()
    profile_p.enter_password(password="Ahoj12345")
    profile_p.conf_delete_button_click()
    
    
    # expected_url = profile_page.expected_delete_acc_url
    # assert profile_page.driver.current_url == expected_url