from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class ExistingEmail:
    def __init__(self, driver):
        self.driver = driver 
        self.SIGNUP_MENU = (By.XPATH, "//a[@href='/login'][contains(.,'Signup / Login')]")
        self.USERNAME_INPUT = (By.XPATH, "//input[contains(@data-qa,'signup-name')]")
        self.EMAIL_INPUT = (By.XPATH, "//input[contains(@data-qa,'signup-email')]")
        self.BTN_SIGN_UP = (By.XPATH, "//button[@type='submit'][contains(.,'Signup')]")
        self.EMAIL_EXIST = (By.XPATH, "//p[contains(.,'Email Address already exist!')]")


    def menu_sign_up(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.SIGNUP_MENU)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn sign up not found")
            return False
        
    def enter_username(self, username):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.USERNAME_INPUT)).send_keys(username)
        except (NoSuchElementException, TimeoutException):
            print("Error: Username input not found")
            return False
        
    def enter_email(self, email):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.EMAIL_INPUT)).send_keys(email)
        except (NoSuchElementException, TimeoutException):
            print("Error: Password input not found")
            return False
        
    def register_sign_up(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.BTN_SIGN_UP)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn sign up not found")
            return False
        
    def get_already_exist(self):
        try:
           element_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.EMAIL_EXIST)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert element_text == "Email Address already exist!", f"Expected 'Email Address already exist!' but got '{element_text}'"