import unittest
from selenium import webdriver
from pages.searchproduct import SearchProduct
import time 

class SearchDemo(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://automationexercise.com')
        self.driver.maximize_window()
        print("page loaded")

    def test_search(self):
        login_page = SearchProduct(self.driver)
        login_page.products()
        print("Main page, Current URL:", self.driver.current_url)
        login_page.search_input("Stylish Dress")
        login_page.search_btn()
        login_page.search_products()
        print("Assertion passed: 'SEARCHED PRODUCTS' text is visible")
        login_page.products_displayed()
        print("Assertion passed: 'SEARCHED PRODUCTS' was found")

    def tearDown(self):
        self.driver.quit()