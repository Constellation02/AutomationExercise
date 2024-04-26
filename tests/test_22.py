import unittest
from selenium import webdriver
from pages.recommended import Recommended
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
        login_page = Recommended(self.driver)
        login_page.scroll_by_amount(0,7500)
        login_page.recommended_items()
        login_page.product_btn()
        login_page.scroll_by_amount(0,0)
        login_page.cart_btn()
        login_page.winter_top()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()