import unittest
from selenium import webdriver
from pages.registeruser import RegisterUser
import time 


class RegisterDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://automationexercise.com')
        self.driver.maximize_window()
        print("page loaded")

    def test_login(self):
        login_page = RegisterUser(self.driver)
        login_page.menu_sign_up()
        print("Click on register/sign up")
        login_page.get_success_message_text()
        print("Assertion passed: 'New User Signup!' text is visible")
        login_page.enter_username("Fabio")
        login_page.enter_email("Laparatuya618@gmail.com")
        login_page.register_sign_up()
        login_page.btn_mr()
        login_page.get_enteraccunt_message()
        print("Assertion passed: 'ENTER ACCOUNT INFORMATION' text is visible")
        print("Click on radio button MR")
        login_page.enter_password("Welcome01")
        login_page.select_date_of_birth('18', '8','1998')
        print("Password & date selected")
        login_page.scroll_by_amount(0, 700)
        login_page.check_box()
        login_page.address_information("Fabio", "Armando", "Cybertron", "Dominican Republic", "Santo Domingo", "Santo Domingo Este", "Santo Domingo Nacional", "10001", "8095556767")
        login_page.select_country("United States")
        login_page.create_btn()
        login_page.get_create_message()
        print("Assertion passed: 'ACCOUNT CREATED!' text is visible")
        login_page.continue_btn()
        login_page.get_logged_as()
        print("Assertion passed: 'Logged in as Fabio Armando' text is visible")
        login_page.delete_btn()
        login_page.get_deleted()
        print("Assertion passed: 'ACCOUNT DELETED!' text is visible")
        time.sleep(10)


        

    


    def tearDown(self):
        self.driver.quit()



