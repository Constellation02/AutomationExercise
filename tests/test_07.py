import unittest
from selenium import webdriver
from pages.casespage import CasesPage
import time 


class ExistingEmailDemo(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://automationexercise.com')
        self.driver.maximize_window()
        print("page loaded")

    def test_testcases(self):
        login_page = CasesPage(self.driver)
        print("Main page, Current URL:", self.driver.current_url)
        login_page.test_cases_btn()
        print("Test case page, Current URL:", self.driver.current_url)
        time.sleep(5)

    
    def tearDown(self):
        self.driver.quit()
        