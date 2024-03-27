import unittest
from selenium import webdriver
from pages.loginuser import LoginUser
import time 


class LoginDemo(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://automationexercise.com')
        self.driver.maximize_window()
        print("page loaded")

    def test_login(self):
        login_page = LoginUser(self.driver)
        login_page.menu_login()
        print("Click on register/sign up")
        login_page.enter_email("Laparatuya5@gmail.com")
        login_page.enter_password("Welcome01")
        login_page.get_Login_text()
        print("Assertion passed: 'Login to your account' text is visible")
        login_page.login_btn()
        login_page.delete_btn()
        print("Click on Delete Btn")
        login_page.deleted()
        print("Assertion passed: 'ACCOUNT DELETED!' text is visible")
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()