from pages.main_page import MainPage

def test_list_of_links(driver):
    main_page = MainPage(driver)
    links = main_page.get_all_links()
    print(links)