import unittest
from selenium import webdriver
from pages.productscart import CartProductss
import time 

class ProductsCartDemo(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://automationexercise.com')
        self.driver.maximize_window()
        print("page loaded")

    def test_search(self):
        login_page = CartProductss(self.driver)
        login_page.products_btn()
        login_page.scroll_by_amount(0,500)
        login_page.selecting_products()
        login_page.cart_btn()
        login_page.price()
        print("Assertion passed: 'Price' text is visible")
        login_page.price02()
        print("Assertion passed: 'Price' text is visible")
        login_page.quantity()
        print("Assertion passed: 'Quantity' text is visible")
        login_page.total01()
        print("Assertion passed: '500' text is visible")
        login_page.total02()
        print("Assertion passed: '400' text is visible")
        print("current page, Current URL:", self.driver.current_url)
        time.sleep(5)
    
    def tearDown(self):
        self.driver.quit()