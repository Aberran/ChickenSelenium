from ..pages.main_page import MainPage
from selenium.webdriver.common.by import By

class RegisterPage(MainPage):
    
    def __init__(self, driver):
        super().__init__(driver)  # This calls MainPage's __init__ method !!!!!!!
        self.go_to_register_page()
        self.email_input = self.driver.find_element(By.XPATH, "//input[@id='id_email']")
        self.first_name_input = self.driver.find_element(By.XPATH, "//input[@id='id_first_name']")
        self.last_name_input = self.driver.find_element(By.XPATH, "//input[@id='id_last_name']")
        self.password1_input = self.driver.find_element(By.XPATH, "//input[@id='id_password1']")
        self.password2_input = self.driver.find_element(By.XPATH, "//input[@id='id_password2']")
        self.submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
   
    def fill_email_input(self, email):
        self.email_input.send_keys(email)
    
    def fill_first_name_input(self, first_name):
        self.first_name_input.send_keys(first_name)
        
    def fill_last_name_input(self, last_name):
        self.last_name_input.send_keys(last_name)
        
    def fill_password1_input(self, password_1):
        self.password1_input.send_keys(password_1)

    def fill_password2_input(self, password_2):
        self.password2_input.send_keys(password_2)
        
    def submit_form(self):
        self.submit_button.click()
    