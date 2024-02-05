import logging
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MainPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.login_button = driver.find_element(By.XPATH, "//a[text()='Log in']")
        self.register_button = driver.find_element(By.XPATH, "//a[text()='Register']")
    
    def go_to_login_page(self):
        self.login_button.click() 
        
    def go_to_register_page(self):
        self.register_button.click() 
    


#actual test
# def test_list_of_links(driver):
#     main_page = MainPage(driver)
#     nav_links = main_page.get_all_links()
#     for link in nav_links:
#         if 'Log in' in link.get_attribute('innerHTML'):
#             link.click()
    
 
    

