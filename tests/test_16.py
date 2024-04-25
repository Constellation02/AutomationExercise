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
        login_page.login_info("testing_production@gmail.com", "Welcome01")
        login_page.get_logged_as()
        print("Assertion passed: 'Logged in as Fabio Armando' text is visible")
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
