import unittest
from selenium import webdriver
from pages.quantityproducts import QuantityProduct
import time 

class QuantityCartDemo(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://automationexercise.com')
        self.driver.maximize_window()
        print("page loaded")
    
    def test_search(self):
        login_page = QuantityProduct(self.driver)
        login_page.scroll_by_amount(0,500)
        login_page.viewproduct_btn()
        print("current page, Current URL:", self.driver.current_url)
        login_page.quantity_input('4')
        login_page.addcart_btn()
        login_page.continue_btn()
        login_page.viewcart_btn()
        login_page.quantity()
        print("Assertion passed: '4' text is visible")
        time.sleep(5)