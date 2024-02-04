from main_page import MainPage
from selenium.webdriver.common.by import By

class LoginPage(MainPage):
    
    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)