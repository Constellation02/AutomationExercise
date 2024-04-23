from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import Select
import time 


class QuantityProduct:
    def __init__(self, driver):
        self.driver = driver
        self.VIEWPRODUCT = (By.XPATH, "//a[@href='/product_details/1'][contains(.,'View Product')]")
        self.ADDTOCAR_BTN = (By.XPATH, "//button[contains(@type,'button')]")
        self.CONTINUE_BTN = (By.XPATH, "//button[contains(@class,'btn btn-success close-modal btn-block')]")
        self.VIEWCART_BTN = (By.XPATH, "//a[@href='/view_cart']")
        self.QUANTITY = (By.XPATH, "//button[@class='disabled'][contains(.,'4')]")
        


    def scroll_by_amount(self, x_pixels, y_pixels):
        """Scroll the window by the given amount."""
        scroll_script = f"window.scrollBy({x_pixels}, {y_pixels})"
        self.driver.execute_script(scroll_script)

    def viewproduct_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.VIEWPRODUCT)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn products not found")
            return False
        
    def quantity_input(self, new_value):
        try:
            quantity_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "quantity")))
            self.driver.execute_script("arguments[0].setAttribute('value', arguments[1])", quantity_input, new_value)
            print("Quantity changed to", new_value)
        except:
            print("Error: Quantity input not found or unable to change value")
        
    def addcart_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ADDTOCAR_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn products not found")
            return False
        
    def continue_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.CONTINUE_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn products not found")
            return False
        
    def viewcart_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.VIEWCART_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn products not found")
            return False
        
    def quantity(self):
        try:
           element_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.QUANTITY)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert element_text == "4", f"Expected '4' but got '{element_text}'"
    