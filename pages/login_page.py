from ..pages.main_page import MainPage
from selenium.webdriver.common.by import By

class LoginPage(MainPage):
    
    def __init__(self, driver):
        super().__init__(driver)  # This calls MainPage's __init__ method !!!!!!!
        self.go_to_login_page()
        self.name_input = self.driver.find_element(By.XPATH, "//input[@name='username']")
        self.password_input = self.driver.find_element(By.XPATH, "//input[@name='password']")
        self.submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
    
    def login(self, username, password):
        self.name_input.send_keys(username)
        self.password_input.send_keys(password)
        self.submit_button.click()
        
        
        
        
    # def fill_name_input(self, username):
    #     self.name_input.send_keys(username)
        
    # def fill_password_input(self, password):
    #     self.password_input.send_keys(password)
        
    # def submit_form(self):
    #     self.submit_button.click()
    