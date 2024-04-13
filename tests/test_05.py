import unittest
from selenium import webdriver
from pages.existingemail import ExistingEmail
import time 

class ExistingEmailDemo(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://automationexercise.com')
        self.driver.maximize_window()
        print("page loaded")


    def test_login(self):
        login_page = ExistingEmail(self.driver)
        login_page.menu_sign_up()
        login_page.enter_username("Fabio")
        login_page.enter_email("Laparatuya1@gmail.com")
        login_page.register_sign_up()
        login_page.get_already_exist()
        print("Assertion passed: 'Email Address already exist!' text is visible")
        time.sleep(5)


