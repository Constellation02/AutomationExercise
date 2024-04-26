import unittest
from selenium import webdriver
from pages.category_products import Category
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
        login_page = Category(self.driver)
        login_page.scroll_by_amount(0,500)
        login_page.womancategory_btn()
        login_page.get_women_products()
        print("Assertion passed: 'WOMEN - DRESS PRODUCTS' text is visible")
        login_page.mencategory_btn()
        login_page.get_men_products()
        print("Assertion passed: 'MEN - JEANS PRODUCTS' text is visible")
        print("current page, Current URL:", self.driver.current_url)
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()

