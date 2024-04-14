from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.alert import Alert

class ContactForm: 
    def __init__(self, driver):
        self.driver = driver
        self.CONTAC_US = (By.XPATH, "//a[@href='/contact_us'][contains(.,'Contact us')]")
        self.GET_IN_TOUCH = (By.XPATH, "//h2[@class='title text-center'][contains(.,'Get In Touch')]")
        self.NAME_INPUT = (By.XPATH, "//input[contains(@data-qa,'name')]")
        self.EMAIL_INPUT = (By.XPATH, "//input[contains(@required,'required')]")
        self.SUBJECT_INPUT = (By.XPATH, "//input[contains(@name,'subject')]")
        self.MESSAGE_INPUT = (By.XPATH, "//textarea[contains(@id,'message')]")
        self.UPLOAD_BTN = (By.XPATH, "//input[contains(@name,'upload_file')]")
        self.SUBMIT_BTN = (By.XPATH, "//input[@data-qa='submit-button']")
        self.SUCCESS_MESSAGE = (By.XPATH,"//div[@class='status alert alert-success'][contains(.,'Success! Your details have been submitted successfully.')]")
        self.HOME_BTN = (By.XPATH, "//span[contains(.,'Home')]")
    

    def contactus(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.CONTAC_US)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn sign up not found")
            return False
        
    def get_in_touch(self):
        try:
           element_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.GET_IN_TOUCH)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert element_text == "GET IN TOUCH", f"Expected 'GET IN TOUCH' but got '{element_text}'"    

    def name(self, username):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.NAME_INPUT)).send_keys(username)
        except (NoSuchElementException, TimeoutException):
            print("Error: Username input not found")
            return False
        
    def email(self, useremail):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.EMAIL_INPUT)).send_keys(useremail)
        except (NoSuchElementException, TimeoutException):
            print("Error: Username input not found")
            return False
    
    def subject(self, usersubject):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.SUBJECT_INPUT)).send_keys(usersubject)
        except (NoSuchElementException, TimeoutException):
            print("Error: Username input not found")
            return False
        
    def message(self, usermessage):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.MESSAGE_INPUT)).send_keys(usermessage)
        except (NoSuchElementException, TimeoutException):
            print("Error: Username input not found")
            return False
        
    def upload_file(self, file_path):
        try:
            upload_element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.UPLOAD_BTN))
            upload_element.send_keys(file_path)
        except (NoSuchElementException, TimeoutException):
            print("Error: Upload button not found")
            return False

    def submit(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.SUBMIT_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn sign up not found")
            return False
    
        
    def handle_alert(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            print("Alert accepted")
        except TimeoutException:
            print("No alert present within the timeout period")
            return False
    
    def success_message(self):
        try:
           element_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert element_text == "Success! Your details have been submitted successfully.", f"Expected 'Success! Your details have been submitted successfully.'{element_text}'"

    def home(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.HOME_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: Home Btn not found")
            return False
