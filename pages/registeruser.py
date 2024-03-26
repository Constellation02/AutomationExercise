from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import Select




class RegisterUser: 
    def __init__(self, driver):
        self.driver = driver 
        self.sign_up_menu = (By.XPATH, "//a[@href='/login'][contains(.,'Signup / Login')]")
        self.username_input = (By.XPATH, "//input[contains(@data-qa,'signup-name')]")
        self.email_input = (By.XPATH, "//input[contains(@data-qa,'signup-email')]")
        self.btn_sign_up = (By.XPATH, "//button[@type='submit'][contains(.,'Signup')]")
        self.SUCCESS_MESSAGE = (By.XPATH, "//h2[contains(., 'New User Signup!')]") # assertion 
        self.BTN_MR = (By.XPATH, "//input[@type='radio'][contains(@id,'gender1')]")
        self.PASSWORD_INPUT = (By.XPATH, "//input[contains(@id,'password')]")
        self.DAY_DROPDOWN = (By.ID, 'days')
        self.MONTH_DROPDOWN = (By.ID, 'months')
        self.YEAR_DROPDOWN = (By.ID, 'years')
        self.BOX1 = (By.XPATH, "//input[contains(@id,'newsletter')]")
        self.BOX2 = (By.XPATH, "//input[contains(@id,'optin')]")
        self.FIRSTNAME_INPUT = (By.XPATH, "//input[contains(@id,'first_name')]")
        self.LASTNAME_INPUT = (By.XPATH, "//input[contains(@data-qa,'last_name')]")
        self.COMPANY_INPUT = (By.XPATH, "//input[contains(@data-qa,'company')]")
        self.ADDRESS_INPUT = (By.XPATH, "//input[@data-qa='address']")
        self.ADDRESS2_INPUT = (By.XPATH, "//input[contains(@data-qa,'address2')]")
        self.COUNTRY = (By.ID, 'country')
        self.STATE_INPUT = (By.XPATH, "//input[contains(@data-qa,'state')]")
        self.CITY_INPUT = (By.XPATH, "//input[contains(@data-qa,'city')]")
        self.ZIPCODE_INPUT = (By.XPATH, "//input[contains(@data-qa,'zipcode')]")
        self.MOBILENUMBER_INPUT = (By.XPATH, "//input[@type='text'][contains(@id,'number')]")
        self.CREATE_ACCOUNT = (By.XPATH, "//button[@type='submit'][contains(.,'Create Account')]")
        self.ENTER_ACCOUNT_MESSAGE = (By.XPATH, "//b[contains(text(), 'Enter Account Information')]")
        self.ACCOUNT_CREATED_B = (By.XPATH, "//b[contains(text(), 'Account Created!')]")
        self.CONTINUE_BTN = (By.XPATH, "//a[@data-qa='continue-button']")
        self.LOGGED_AS = (By.XPATH, "//a[contains(.,'Logged in as Fabio Armando')]")
        self.DELETE_BTN = (By.XPATH, "//a[@href='/delete_account'][contains(.,'Delete Account')]")
        self.ACCOUNT_DELETED_B = (By.XPATH, "//b[text()='Account Deleted!']")

        
    
    def get_success_message_text(self):
        try:
           element_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert element_text == "New User Signup!", f"Expected 'New User Signup!' but got '{element_text}'"

    def get_enteraccunt_message(self):
        try:
           acct_text01 = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ENTER_ACCOUNT_MESSAGE)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert acct_text01 == "ENTER ACCOUNT INFORMATION", f"Expected 'ENTER ACCOUNT INFORMATION' but got '{acct_text01}'"

    def get_create_message(self):
        try:
           create_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ACCOUNT_CREATED_B)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert create_text == "ACCOUNT CREATED!", f"Expected 'ACCOUNT CREATED!' but got '{create_text}'"

    def get_logged_as(self):
        try:
           logged_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.LOGGED_AS)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert logged_text == "Logged in as Fabio Armando", f"Expected 'Logged in as Fabio Armando' but got '{logged_text}'"

    def get_deleted(self):
        try:
           delete_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ACCOUNT_DELETED_B)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert delete_text == "ACCOUNT DELETED!", f"Expected 'ACCOUNT DELETED!' but got '{delete_text}'"
        
    
    def menu_sign_up(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.sign_up_menu)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn sign up not found")
            return False

    def enter_username(self, username):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.username_input)).send_keys(username)
        except (NoSuchElementException, TimeoutException):
            print("Error: Username input not found")
            return False
    
    def enter_email(self, password):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.email_input)).send_keys(password)
        except (NoSuchElementException, TimeoutException):
            print("Error: Password input not found")
            return False
        
    def register_sign_up(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.btn_sign_up)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn sign up not found")
            return False
    
    def btn_mr(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.BTN_MR)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn sign up not found")
            return False
        
    def enter_password(self, password):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PASSWORD_INPUT)).send_keys(password)
        except (NoSuchElementException, TimeoutException):
            print("Error: password space no found")
            return False
        
    def select_date_of_birth(self, day, month, year):
        Select(self.driver.find_element(*self.DAY_DROPDOWN)).select_by_index(day)
        Select(self.driver.find_element(*self.MONTH_DROPDOWN)).select_by_index(month)
        Select(self.driver.find_element(*self.YEAR_DROPDOWN)).select_by_value(year)

    def select_country(self, state):
        Select(self.driver.find_element(*self.COUNTRY)).select_by_value(state)

    def check_box(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.BOX1)).click()
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.BOX2)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: check box not found")
            return False
        
   
    def scroll_by_amount(self, x_pixels, y_pixels):
        """Scroll the window by the given amount."""
        scroll_script = f"window.scrollBy({x_pixels}, {y_pixels})"
        self.driver.execute_script(scroll_script)
    
        
    def address_information(self, first_name, last_name, company, address, address2, state, city, zipcode, mobile_number):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.FIRSTNAME_INPUT)).send_keys(first_name)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.LASTNAME_INPUT)).send_keys(last_name)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.COMPANY_INPUT)).send_keys(company)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ADDRESS_INPUT)).send_keys(address)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ADDRESS2_INPUT)).send_keys(address2)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.STATE_INPUT)).send_keys(state)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.CITY_INPUT)).send_keys(city)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ZIPCODE_INPUT)).send_keys(zipcode)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.MOBILENUMBER_INPUT)).send_keys(mobile_number)
        except (NoSuchElementException, TimeoutException):
            print("Error: Username input not found")
            return False
        

    def create_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.CREATE_ACCOUNT)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: Acct btn sign up not found")
            return False
        
    def continue_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.CONTINUE_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn sign up not found")
            return False
        
    def delete_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.DELETE_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn sign up not found")
            return False
    
    
    
        




