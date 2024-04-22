from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

class Subscription:
    def __init__(self, driver):
        self.driver = driver
        self.SUBSCRIPTION = (By.XPATH, "//h2[contains(.,'Subscription')]")
        self.EMAIL_INPUT = (By.XPATH, "//input[contains(@id,'susbscribe_email')]")
        self.EMAIL_BTN = (By.XPATH, "//button[contains(@id,'subscribe')]")
        self.SUBSCRIPTION_SENT = (By.XPATH, "//div[contains(@class,'alert-success alert')]")
        self.CART_BTN = (By.XPATH, "//a[@href='/view_cart'][contains(.,'Cart')]")
        

    def scroll_by_amount(self, x_pixels, y_pixels):
        """Scroll the window by the given amount."""
        scroll_script = f"window.scrollBy({x_pixels}, {y_pixels})"
        self.driver.execute_script(scroll_script)

    def get_subscrition_message_text(self):
        try:
           element_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.SUBSCRIPTION)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert element_text == "SUBSCRIPTION", f"Expected 'SUBSCRIPTION' but got '{element_text}'"

    def enter_email(self, email):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.EMAIL_INPUT)).send_keys(email)
        except (NoSuchElementException, TimeoutException):
            print("Error: email input not found")
            return False
        
    def email_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.EMAIL_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error:  btn not found")
            return False
        
    def cart_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.CART_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error:  btn not found")
            return False
        
    def get_success_message_text(self):
        try:
           element_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.SUBSCRIPTION_SENT)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert element_text == "You have been successfully subscribed!", f"Expected 'You have been successfully subscribed!' but got '{element_text}'"