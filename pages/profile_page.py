import logging
from selenium.webdriver.common.by import By
from ..pages.main_page import MainPage


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProfilePage(MainPage):
    
    def __init__(self, driver):
        self.driver = driver
        self.profile_page_url = "http://127.0.0.1:8000/user-profile"
        self.profile_button = driver.find_element(By.XPATH, "//a[text()='Profile']")
        self.edit_button = driver.find_element(By.XPATH, "//button[text()='Edit profile']")
        self.delete_acc_button = driver.find_element(By.XPATH, "//button[text()='Delete Account']")
        self.conf_pass_input = driver.find_element(By.XPATH, "//input[@id='id_passwword_confirmation']")
        self.conf_delete_button = driver.find_element(By.XPATH, "//button[text()='Confirm Delete Account']")
        self.expected_delete_acc_url = "http://127.0.0.1:8000/bye"
        
    def profile_button_click(self):
        self.profile_button.click()
    
    def edit_button_click(self):
        self.edit_button.click()
    
    def delete_acc_button_click(self):
        self.delete_acc_button.click()
        
    def enter_password(self, password):
        self.conf_pass_input.send_keys(password)
        
    def conf_delete_button_click(self):
        self.conf_delete_button.click()
        
         