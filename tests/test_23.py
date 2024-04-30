import unittest
from selenium import webdriver
from pages.addressdetails import Address
import time 

class PlaceOrderDemo(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://automationexercise.com')
        self.driver.maximize_window()
        print("page loaded")
    
    def test_recommended(self):
        login_page = Address(self.driver)
        login_page.signup_login_btn()
        login_page.credentials("Testingg", "testing11_production004@gmail.com")
        login_page.btn_mr()
        login_page.scroll_by_amount(0,500)
        login_page.enter_password("Welcome01")
        login_page.select_date_of_birth('18', '8','1998')
        print("Password & date selected")
        login_page.check_box()
        login_page.address_information("Fabio", "Armando", "Cybertron", "Dominican Republic", "Santo Domingo", "Santo Domingo Este", "Santo Domingo Nacional", "10001", "8095556767")
        login_page.scroll_by_amount(0,300)
        login_page.create_btn()
        login_page.get_create_message()
        print("Assertion passed: 'ACCOUNT CREATED!' text is visible")
        login_page.continue_btn()
        login_page.get_logged_as()
        print("Assertion passed: 'Logged in as Fabio Armando' text is visible")
        login_page.home_btn()
        login_page.scroll_by_amount(0,500)
        login_page.selecting_products()
        login_page.cart_btn()
        print("current page, Current URL:", self.driver.current_url)
        login_page.checkout_btn()
        login_page.verify_delivery_address()
        login_page.btn_delete_acct()
        login_page.get_deleted_message()
        time.sleep(5)


    def tearDown(self):
        self.driver.quit()