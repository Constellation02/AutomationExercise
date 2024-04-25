import unittest
from selenium import webdriver
from pages.productscart import CartProductss
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
        login_page = CartProductss(self.driver)
        login_page.scroll_by_amount(0,500)
        login_page.selecting_products()
        login_page.cart_btn()
        print("current page, Current URL:", self.driver.current_url)
        login_page.eliminate_products_btn()
        login_page.cart_empty()
        print("Assertion passed: 'Cart is empty!' text is visible")

        

    def tearDown(self):
        self.driver.quit()