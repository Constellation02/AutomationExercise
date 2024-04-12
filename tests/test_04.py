import unittest
from selenium import webdriver
from pages.logoutuser import LogoutUser
import time


class LogoutDemo(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://automationexercise.com')
        self.driver.maximize_window()
        print("page loaded")

    def test_logout(self):
        login_page = LogoutUser(self.driver)
        login_page.menu_login()
        print("Click on register/sign up")
        login_page.enter_email("Laparatuya1@gmail.com")
        login_page.enter_password("Welcome01")
        login_page.login_btn()
        login_page.logged_as()
        print("Assertion passed: 'Logged in as Fabio Armando' text is visible")
        login_page.logout_btn()
        print("Logged out, Current URL:", self.driver.current_url)
        time.sleep(10)
        


    def tearDown(self):
        self.driver.quit()
