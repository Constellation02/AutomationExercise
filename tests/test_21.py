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
        login_page.products_btn()
        print("current page, Current URL:", self.driver.current_url)
        login_page.scroll_by_amount(0,400)
        login_page.view_product()
        login_page.scroll_by_amount(0,500)
        login_page.write_review("Fabio", "testing@gmail.com", "This is a good product")
        login_page.get_thank_u()
        print("Assertion passed: 'Thank you for your review.' text is visible")
        time.sleep(10)


    def tearDown(self):
        self.driver.quit()