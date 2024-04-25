import unittest
from selenium import webdriver
from pages.placeorder import PlaceOrder
import time 

class PlaceOrderDemo(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://automationexercise.com')
        self.driver.maximize_window()
        print("page loaded")
    
    def test_search(self):
        login_page = PlaceOrder(self.driver)
        login_page.signup_login_btn()
        login_page.enter_username("Testing")
        login_page.enter_email("testing_production77@gmail.com")
        login_page.register_sign_up()
        login_page.btn_mr()
        login_page.scroll_by_amount(0,500)
        login_page.enter_password("Welcome01")
        login_page.select_date_of_birth('18', '8','1998')
        print("Password & date selected")
        login_page.check_box()
        login_page.address_information("Fabio", "Armando", "Cybertron", "Dominican Republic", "Santo Domingo", "Santo Domingo Este", "Santo Domingo Nacional", "10001", "8095556767")
        login_page.scroll_by_amount(0,200)
        login_page.create_btn()
        login_page.get_create_message()
        print("Assertion passed: 'ACCOUNT CREATED!' text is visible")
        login_page.get_logged_as()
        print("Assertion passed: 'Logged in as Fabio Armando' text is visible")
        login_page.home_btn()
        login_page.scroll_by_amount(0,500)
        login_page.selecting_products()
        login_page.cart_btn()
        print("current page, Current URL:", self.driver.current_url)
        login_page.checkout_btn()
        login_page.scroll_by_amount(0,800)
        login_page.checkout_btn()
        login_page.enter_card_info("testing", "4445111225587", "311", "10", "2026")
        login_page.pay_n_confirm_btn()
        login_page.get_orderconfirmed_message()
        print("Assertion passed: 'Your order has been placed successfully!' text is visible")
        login_page.delete_btn()
        login_page.get_deleted()
        print("Assertion passed: 'ACCOUNT DELETED!' text is visible")
        login_page.final_continue_btn()
        time.sleep(10)
        
    def tearDown(self):
        self.driver.quit()