from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import Select
import time




class Category: 
    def __init__(self, driver):
        self.driver = driver 
        self.WOMEN = (By.XPATH, "//a[@href='#Women']")
        self.DRESS = (By.XPATH, "//a[@href='/category_products/1']")
        self.WOMEN_DRESS_TEXT = (By.XPATH, "//h2[@class='title text-center'][contains(.,'Women - Dress Products')]")
        self.MEN = (By.XPATH, "//a[@href='#Men']")
        self.JEANS = (By.XPATH, "//a[@href='/category_products/6']")
        self.MEN_JEANS_TEXT = (By.XPATH, "//h2[@class='title text-center'][contains(.,'Men - Jeans Products')]")
        self.PRODUCTS_BTN = (By.XPATH, "//a[@href='/products']")
        self.BRANDS_TEXT = (By.XPATH, "//h2[contains(.,'Brands')]")
        self.POLO_BTN = (By.XPATH, "//a[@href='/brand_products/Polo']")
        self.POLO_TEXT = (By.XPATH, "//h2[@class='title text-center'][contains(.,'Brand - Polo Products')]")
        self.SEARCH_PRODUCT = (By.XPATH, "//input[contains(@id,'search_product')]")
        self.SEARCH_BTN = (By.XPATH, "//button[contains(@id,'submit_search')]")
        self.SEARCHED_PRODUCTS = (By.XPATH, "//h2[@class='title text-center'][contains(.,'Searched Products')]")
        self.PREMIUN_POLO = (By.XPATH, "(//p[contains(.,'Premium Polo T-Shirts')])[2]")
        self.PREMIUN_POLO2 = (By.XPATH, "//a[@href='/product_details/30'][contains(.,'Premium Polo T-Shirts')]")
        self.ADD_CART = (By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/a")
        self.VIEWCART = (By.XPATH, "//u[contains(.,'View Cart')]")
        self.SIGNUP_LOGIN = (By.XPATH, "//a[@href='/login'][contains(.,'Signup / Login')]")
        self.EMAIL_ACCT = (By.XPATH, "//input[contains(@data-qa,'login-email')]")
        self.PASSWORD_ACCT = (By.XPATH, "//input[contains(@type,'password')]")
        self.GO_BACK_TO_CART = (By.XPATH, "//a[@href='/view_cart'][contains(.,'Cart')]")
        self.VIEW_PRODUCT = (By.XPATH, "//a[@href='/product_details/1'][contains(.,'View Product')]")
        self.NAME = (By.XPATH, "//input[contains(@id,'name')]")
        self.EMAIL_ADDRESS = (By.XPATH, "//input[@id='email']")
        self.ADD_REVIEW = (By.XPATH, "//textarea[contains(@id,'review')]")
        self.SUBMIT = (By.XPATH, "//button[contains(@id,'button-review')]")
        self.THANK_U = (By.XPATH, "//span[contains(.,'Thank you for your review.')]")


    def womancategory_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.WOMEN)).click()
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.DRESS)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn products not found")
            return False
        
    def scroll_by_amount(self, x_pixels, y_pixels):
        """Scroll the window by the given amount."""
        scroll_script = f"window.scrollBy({x_pixels}, {y_pixels})"
        self.driver.execute_script(scroll_script)

    def get_women_products(self):
        try:
           delete_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.WOMEN_DRESS_TEXT)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert delete_text == "WOMEN - DRESS PRODUCTS", f"Expected 'WOMEN - DRESS PRODUCTS'' but got '{delete_text}'"
    
    def mencategory_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.MEN)).click()
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.JEANS)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn products not found")
            return False

    def get_men_products(self):
        try:
           delete_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.MEN_JEANS_TEXT)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert delete_text == "MEN - JEANS PRODUCTS", f"Expected 'MEN - JEANS PRODUCTS'' but got '{delete_text}'"    
    
    def products_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PRODUCTS_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn products not found")
            return False
    
    def get_brands(self):
        try:
           delete_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.BRANDS_TEXT)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert delete_text == "BRANDS", f"Expected 'BRANDS'' but got '{delete_text}'" 

    def polo_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.POLO_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn products not found")
            return False   
        
    def get_polo_products(self):
        try:
           delete_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.POLO_TEXT)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert delete_text == "BRAND - POLO PRODUCTS", f"Expected 'BRAND - POLO PRODUCTS'' but got '{delete_text}'"

    def search(self, product):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.SEARCH_PRODUCT)).send_keys(product)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.SEARCH_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn products not found")
            return False
        
    def get_searched_products(self):
        try:
           delete_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.SEARCHED_PRODUCTS)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert delete_text == "SEARCHED PRODUCTS", f"Expected 'SEARCHED PRODUCTS'' but got '{delete_text}'"

    def get_premium_polo(self):
        try:
           delete_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PREMIUN_POLO)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert delete_text == "Premium Polo T-Shirts", f"Expected 'Premium Polo T-Shirts'' but got '{delete_text}'"

    def productadd_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ADD_CART)).click()
            time.sleep(2)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.VIEWCART)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: btn products not found")
            return False
        
    def get_premium_polo2(self):
        try:
           delete_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PREMIUN_POLO2)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert delete_text == "Premium Polo T-Shirts", f"Expected 'Premium Polo T-Shirts'' but got '{delete_text}'"

    def signupandlogin_btn(self, email, password):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.SIGNUP_LOGIN)).click()
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.EMAIL_ACCT)).send_keys(email)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PASSWORD_ACCT)).send_keys(password)
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn products not found")
            return False
        
    def go_back_to_cart_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.GO_BACK_TO_CART)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn products not found")
            return False
    
    def view_product(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.VIEW_PRODUCT)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn products not found")
            return False
        
    def write_review(self, name, email, review):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.NAME)).send_keys(name)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.EMAIL_ADDRESS)).send_keys(email)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ADD_REVIEW)).send_keys(review)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.SUBMIT)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn products not found")
            return False
        
    def get_thank_u(self):
        try:
           delete_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.THANK_U)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert delete_text == "Thank you for your review.", f"Expected 'Thank you for your review.'' but got '{delete_text}'"