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
        login_page.search("Premium Polo T-Shirts")
        login_page.get_searched_products()
        print("Assertion passed: 'SEARCHED PRODUCTS' text is visible")
        login_page.get_premium_polo()
        print("Assertion passed: 'Premium Polo T-Shirts' text is visible")
        login_page.scroll_by_amount(0,400)
        login_page.productadd_btn()
        login_page.get_premium_polo2()
        print("Assertion passed: 'Premium Polo T-Shirts' text is visible")
        login_page.signupandlogin_btn("testing_production@gmail.com", "Welcome01")
        login_page.go_back_to_cart_btn()
        login_page.get_premium_polo2()
        print("Assertion passed: 'Premium Polo T-Shirts' text is visible")
        time.sleep(1)


    
    def tearDown(self):
        self.driver.quit()