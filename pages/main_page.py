from selenium.webdriver.common.by import By

class MainPage:
    
    def __init__(self, driver):
        self.driver = driver
        
    def get_all_links(self):
        links = self.driver.find_elements(By.XPATH, value="//*[@href]")
        return links
        