import unittest
from selenium import webdriver
from pages.download import Download
import time 

class QuantityCartDemo(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://automationexercise.com')
        self.driver.maximize_window()
        print("page loaded")
    
    def test_download(self):
        login_page = Download(self.driver)
        login_page.scroll_by_amount(0,500)
        login_page.selecting_products()
        login_page.scroll_by_amount(0,0)
        login_page.cart_btn()
        print("current page, Current URL:", self.driver.current_url)
        login_page.placeorder_btn()
        login_page.credentials("Testing", "testing_production5800@gmail.com")
        login_page.btn_mr()
        login_page.enter_password("Welcome01")
        login_page.select_date_of_birth('18', '8','1998')
        login_page.check_box()
        login_page.scroll_by_amount(0,300)
        login_page.address_information("Fabio", "Armando", "Cybertron", "Dominican Republic", "Santo Domingo", "Santo Domingo Este", "Santo Domingo Nacional", "10001", "8095556767")
        login_page.select_country('United States')
        login_page.create_btn()
        login_page.get_logged_as()
        print("Assertion passed: 'Logged in as Fabio Armando' text is visible")
        login_page.cart_btn()
        login_page.placeorder_btn()
        login_page.verify_delivery_address()
        login_page.scroll_by_amount(0,900)
        login_page.enter_comment("I really Love this product")
        login_page.enter_card_info("testing", "4445111225587", "311", "10", "2026")
        login_page.pay_n_confirm_btn()
        login_page.download_btn()
        login_page.continue_order_btn()
        login_page.delete_btn()
        login_page.get_deleted()
        print("Assertion passed: 'ACCOUNT DELETED!' text is visible")
        login_page.final_continue_btn()
        time.sleep(5)

    

    def tearDown(self):
        self.driver.quit()