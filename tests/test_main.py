from ..pages.main_page import MainPage

def test_log_in_page(driver):
    main_page = MainPage(driver)
    main_page.go_to_login_page()
    
def test_register_page(driver):
    main_page = MainPage(driver)
    main_page.go_to_register_page()