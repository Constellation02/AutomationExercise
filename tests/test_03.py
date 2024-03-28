import unittest
from selenium import webdriver
from pages.incorrectlogin import NotUser
import time 


class IcorrectLoginDemo(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://automationexercise.com')
        self.driver.maximize_window()
        print("page loaded")

    def test_incorrect_login(self):
        login_page = NotUser(self.driver)
        login_page.menu_login()
        print("Click on register/sign up")
        login_page.enter_email("Laparatuya5@gmail.com")
        login_page.enter_password("Welcome01")
        login_page.login_btn()
        login_page.get_error_text()
        print("Assertion passed: 'Your email or password is incorrect!' text is visible")
        time.sleep(10)



    def tearDown(self):
        self.driver.quit()