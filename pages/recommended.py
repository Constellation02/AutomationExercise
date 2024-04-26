from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time 


class Recommended:
    def __init__(self, driver):
        self.driver = driver
        self.RECOMMENDED_ITEMS = (By.XPATH, "//h2[@class='title text-center'][contains(.,'recommended items')]")
        self.PRODUCT_BTN = (By.XPATH, "(//a[@data-product-id='5'][contains(.,'Add to cart')])[3]")
        self.CONTINUE_BTN = (By.XPATH, "//button[contains(@class,'btn btn-success close-modal btn-block')]")
        self.CART_BTN = (By.XPATH, "(//a[@href='/view_cart'])[1]")
        self.WINTER_TOP = (By.XPATH, "//a[@href='/product_details/5'][contains(.,'Winter Top')]")



    def scroll_by_amount(self, x_pixels, y_pixels):
        """Scroll the window by the given amount."""
        scroll_script = f"window.scrollBy({x_pixels}, {y_pixels})"
        self.driver.execute_script(scroll_script)

    def recommended_items(self):
        try:
           element_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.RECOMMENDED_ITEMS)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert element_text == "RECOMMENDED ITEMS", f"Expected 'RECOMMENDED ITEMS' but got '{element_text}'"

    def product_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PRODUCT_BTN)).click()
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.CONTINUE_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn products not found")
            return False
        
    def cart_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.CART_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn products not found")
            return False
        
    def winter_top(self):
        try:
           element_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.WINTER_TOP)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert element_text == "Winter Top", f"Expected 'Winter Top' but got '{element_text}'"