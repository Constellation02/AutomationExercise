from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import Select


class NotUser: 
    def __init__(self, driver):
        self.driver = driver
        self.SIGNUP_MENU = (By.XPATH, "//a[@href='/login'][contains(.,'Signup / Login')]")
        self.EMAIL_INPUT = (By.XPATH, "//input[contains(@data-qa,'login-email')]")
        self.PASSWORD_INPUT = (By.XPATH, "//input[contains(@type,'password')]")
        self.BTN_LOGIN = (By.XPATH, "//button[@type='submit'][contains(.,'Login')]")
        self.TEXT_INCORRECT = (By.XPATH, "//p[contains(.,'Your email or password is incorrect!')]")



    def menu_login(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.SIGNUP_MENU)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn sign up not found")
            return False
        
    def enter_email(self, email):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.EMAIL_INPUT)).send_keys(email)
        except (NoSuchElementException, TimeoutException):
            print("Error: email input not found")
            return False
        
    def enter_password(self, password):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PASSWORD_INPUT)).send_keys(password)
        except (NoSuchElementException, TimeoutException):
            print("Error: email input not found")
            return False
        
    def login_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.BTN_LOGIN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: btn login not found")
            return False
        
    def get_error_text(self):
        try:
           login_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.TEXT_INCORRECT)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert login_text == "Your email or password is incorrect!", f"Expected 'Your email or password is incorrect!' but got '{login_text}'"