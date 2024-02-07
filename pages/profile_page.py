import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProfilePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.profile_page_url = "http://127.0.0.1:8000/user-profile"
    
    @property
    def profile_button(self):
        return self.driver.find_element(By.XPATH, "//a[text()='Profile']")
    
    @property
    def edit_button(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Edit profile']")
    
    @property
    def delete_acc_button(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Delete Account']")
    
    @property
    def conf_pass_input(self):
        return self.driver.find_element(By.XPATH, "//input[@id='id_password_confirmation']")  # Corrected the typo here
    
    @property
    def conf_delete_button(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Confirm Delete Account']")
    
    def visit_profile_page(self):
        self.driver.get(self.profile_page_url)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of(self.profile_button)
        )
        logger.info("Navigated to Profile Page")
        

    
   
    
    def edit_button_click(self):
        self.edit_button.click()
    
    def delete_acc_button_click(self):
        self.delete_acc_button.click()
        
    def enter_password(self, password):
        self.conf_pass_input.send_keys(password)
        
    def conf_delete_button_click(self):
        self.conf_delete_button.click()
        
         