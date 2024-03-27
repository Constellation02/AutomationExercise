from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import Select

class LoginUser: 
    def __init__(self, driver):
        self.driver = driver 
        self.SIGNUP_MENU = (By.XPATH, "//a[@href='/login'][contains(.,'Signup / Login')]")
        self.LOGIN_TEXT = (By.XPATH, "//h2[contains(., 'Login to your account')]")
        self.EMAIL_INPUT = (By.XPATH, "//input[contains(@data-qa,'login-email')]")
        self.PASSWORD_INPUT = (By.XPATH, "//input[contains(@type,'password')]")
        self.BTN_LOGIN = (By.XPATH, "//button[@type='submit'][contains(.,'Login')]")
        self.LOGIN_AS = (By.XPATH, "//a[contains(.,'Logged in as Fabio')]")
        self.BTN_DELETE = (By.XPATH, "//a[@href='/delete_account'][contains(.,'Delete Account')]")
        self.DELETED_TEXT = (By.XPATH, "//b[text()='Account Deleted!']")


    def menu_login(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.SIGNUP_MENU)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn sign up not found")
            return False
        
    def get_Login_text(self):
        try:
           login_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.LOGIN_TEXT)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert login_text == "Login to your account", f"Expected 'Login to your account' but got '{login_text}'"

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

    def logged_as(self):
        try:
           logged_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.LOGIN_AS)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert logged_text == "Logged in as Fabio Armando", f"Expected 'Logged in as Fabio Armando' but got '{logged_text}'"
    
    def delete_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.BTN_DELETE)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: btn delete not found")
            return False
        
    def deleted(self):
        try:
           delete_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.DELETED_TEXT)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert delete_text == "ACCOUNT DELETED!", f"Expected 'ACCOUNT DELETED!' but got '{delete_text}'"