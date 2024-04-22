from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class SearchProduct:
    def __init__(self, driver):
        self.driver = driver 
        self.PRODUCTS_BTN = (By.XPATH, "//a[@href='/products']")
        self.SEARCH_INPUT = (By.XPATH, "//input[@id='search_product']")
        self.SEARCH_BTN = (By.XPATH, "//i[contains(@class,'fa fa-search')]")
        self.SEARCH_PRODUCTS = (By.XPATH, "//h2[@class='title text-center'][contains(.,'Searched Products')]")
        self.STYLISH_DRESS = (By.XPATH, "(//p[contains(.,'Stylish Dress')])[2]")



    def products(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PRODUCTS_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: btn not found")
            return False
    
    def search_input(self, product_name):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.SEARCH_INPUT)).send_keys(product_name)
        except (NoSuchElementException, TimeoutException):
            print("Error: Search input not found")
            return False
        
    def search_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.SEARCH_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: btn not found")
            return False
        
    def search_products(self):
        try:
           element_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.SEARCH_PRODUCTS)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert element_text == "SEARCHED PRODUCTS", f"Expected 'SEARCHED PRODUCTS' but got '{element_text}'"

    def products_displayed(self):
        try:
            product_01_displayed = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.STYLISH_DRESS)).is_displayed()

            if product_01_displayed:
                print("The product is displayed")
                return True
            else:
                print("The product is not displayed")
                return False
        except (NoSuchElementException, TimeoutException):
            print("Error: Products not found")
            return False