from ..pages.login_page import LoginPage
import logging
import pytest

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# username = 'sele@sele.com'
# password = 'Ahoj12345'
    
@pytest.mark.parametrize("username, password", [ ("sele@sele.com", "Ahoj12345"),
                                                 ("test1", "test1"),
                                                 ("test2", "test2"),
                                                ])
def test_log_in(driver, username, password):
    
    login_page = LoginPage(driver)
    login_page.fill_name_input(username=username)
    login_page.fill_password_input(password=password)
    login_page.submit_form()
    
    expected_url = "http://127.0.0.1:8000/"
    assert driver.current_url == expected_url