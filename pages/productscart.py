from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time 


class CartProductss:
    def __init__(self, driver):
        self.driver = driver
        self.PRODUCT_BTN = (By.XPATH, "//a[@href='/products']")
        self.PRODUCT_01 = (By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/a")
        self.PRODUCT_02 = (By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]/a")
        self.CONTINUE_BTN = (By.XPATH, "//button[contains(.,'Continue Shopping')]")
        self.CART_BTN = (By.XPATH, "//i[contains(@class,'fa fa-shopping-cart')]")
        self.PRICE = (By.XPATH, "(//p[contains(.,'Rs. 500')])[1]")
        self.PRICE02 = (By.XPATH, "(//p[contains(.,'Rs. 400')])[1]")
        self.QUANTITY = (By.XPATH, "(//button[contains(.,'1')])[1]")
        self.TOTAL01 = (By.XPATH, "//p[@class='cart_total_price'][contains(.,'Rs. 500')]")
        self.TOTAL02 = (By.XPATH, "//p[@class='cart_total_price'][contains(.,'Rs. 400')]")

    def products_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PRODUCT_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn products not found")
            return False
        
    def selecting_products(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PRODUCT_01)).click()
            time.sleep(2)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.CONTINUE_BTN)).click()
            time.sleep(2)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PRODUCT_02)).click()
            time.sleep(2)
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
        
    def scroll_by_amount(self, x_pixels, y_pixels):
        """Scroll the window by the given amount."""
        scroll_script = f"window.scrollBy({x_pixels}, {y_pixels})"
        self.driver.execute_script(scroll_script)

    def price(self):
        try:
           element_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PRICE)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert element_text == "Rs. 500", f"Expected 'Rs. 500' but got '{element_text}'"

    def price02(self):
        try:
           element_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PRICE02)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert element_text == "Rs. 400", f"Expected 'Rs. 400' but got '{element_text}'"

    def quantity(self):
        try:
           element_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.QUANTITY)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert element_text == "1", f"Expected '1' but got '{element_text}'"

    def total01(self):
        try:
           element_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.TOTAL01)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert element_text == "Rs. 500", f"Expected 'Rs. 500' but got '{element_text}'"

    def total02(self):
        try:
           element_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.TOTAL02)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert element_text == "Rs. 400", f"Expected 'Rs. 400' but got '{element_text}'"
        
