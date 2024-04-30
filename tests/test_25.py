import unittest
from selenium import webdriver
from pages.subscription import Subscription
import time 


class RegisterDemo(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://automationexercise.com')
        self.driver.maximize_window()
        print("page loaded")

    def test_subscrition(self):
        login_page = Subscription(self.driver)
        print("Main page, Current URL:", self.driver.current_url)
        login_page.scroll_by_amount(0,8500)
        login_page.get_subscrition_message_text()
        print("Assertion passed: 'subscrition' text is visible")
        login_page.arrowup_btn()
        login_page.get_title_text()
        print("Assertion passed: 'Full-Fledged practice website for Automation Engineers' text is visible")
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()