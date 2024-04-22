import unittest
from selenium import webdriver
from pages.products import Products
import time 

class ExistingEmailDemo(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://automationexercise.com')
        self.driver.maximize_window()
        print("page loaded")

    def test_products(self):
        login_page = Products(self.driver)
        print("Main page, Current URL:", self.driver.current_url)
        login_page.products()
        print("Main page, Current URL:", self.driver.current_url)
        login_page.products_displayed()
        time.sleep(5)
        login_page.scroll_by_amount(0, 700)
        login_page.product_01()
        print("product 01 displayed")
        print("Main page, Current URL:", self.driver.current_url)
        login_page.product_name()
        print("Assertion passed: 'Blue Top' text is visible")
        login_page.category()
        print("Assertion passed: 'Category' text is visible")
        login_page.price()
        print("Assertion passed: 'Price' text is visible")
        login_page.availability()
        print("Assertion passed: 'availability' text is visible")
        login_page.condition()
        print("Assertion passed: 'condition' text is visible")
        login_page.brand()
        print("Assertion passed: 'brand' text is visible")
        time.sleep(5)
    
    def tearDown(self):
        self.driver.quit()