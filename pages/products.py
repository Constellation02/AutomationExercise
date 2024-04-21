from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class Products:
    def __init__(self, driver):
        self.driver = driver
        self.PRODUCTS_BTN = (By.XPATH, "//a[@href='/products']")
        self.ALL_PRODUCTS = (By.XPATH, "//h2[@class='title text-center'][contains(.,'All Products')]")
        self.PRODUCT_01 = (By.XPATH, "(//div[@class='product-overlay'])[1]")
        self.PRODUCT_02 = (By.XPATH, "(//div[@class='product-overlay'])[2]")
        self.PRODUCT_03 = (By.XPATH, "(//div[@class='product-overlay'])[3]")
        self.PRODUCT01_BTN = (By.XPATH, "//a[@href='/product_details/1'][contains(.,'View Product')]")
        self.PRODUCT_NAME = (By.XPATH, "//h2[contains(.,'Blue Top')]")
        self.CATEGORY = (By.XPATH, "//p[contains(.,'Category: Women > Tops')]")
        self.PRICE = (By.XPATH, "(//span[contains(.,'Rs. 500')])[2]")
        self.AVAILABILITY = (By.XPATH, "//b[contains(.,'Availability:')]")
        self.CONDITION = (By.XPATH, "//b[contains(.,'Condition:')]")
        self.BRAND = (By.XPATH, "//b[contains(.,'Brand:')]")



    def products(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PRODUCTS_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: btn not found")
            return False
        
    def all_products(self):
        try:
           element_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ALL_PRODUCTS)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert element_text == "All Products", f"Expected 'All Products' but got '{element_text}'"

    def products_displayed(self):
        try:
            product_01_displayed = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PRODUCT_01)).is_displayed()
            product_02_displayed = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PRODUCT_02)).is_displayed()
            product_03_displayed = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PRODUCT_03)).is_displayed()

            if product_01_displayed and product_02_displayed and product_03_displayed:
                print("All products are displayed")
                return True
            else:
                print("Not all products are displayed")
                return False
        except (NoSuchElementException, TimeoutException):
            print("Error: Products not found")
            return False
        
    def product_01(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PRODUCT01_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: btn not found")
            return False 
        
    def product_name(self):
        try:
           element_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PRODUCT_NAME)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert element_text == "Blue Top", f"Expected 'Blue Top' but got '{element_text}'"

    def category(self):
        try:
           element_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.CATEGORY)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert element_text == "Category: Women > Tops", f"Expected 'Category: Women > Tops' but got '{element_text}'"

    def price(self):
        try:
           element_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PRICE)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert element_text == "Rs. 500", f"Expected 'Rs. 500' but got '{element_text}'"

    def availability(self):
        try:
           element_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.AVAILABILITY)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert element_text == "Availability:", f"Expected 'Availability:' but got '{element_text}'"

    def condition(self):
        try:
           element_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.CONDITION)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert element_text == "Condition:", f"Expected 'Condition:' but got '{element_text}'"

    def brand(self):
        try:
           element_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.BRAND)).text
        except(NoSuchElementException, TimeoutException):
            print("Error: No text found!")
            return False
        assert element_text == "Brand:", f"Expected 'Brand:' but got '{element_text}'"

    def scroll_by_amount(self, x_pixels, y_pixels):
        """Scroll the window by the given amount."""
        scroll_script = f"window.scrollBy({x_pixels}, {y_pixels})"
        self.driver.execute_script(scroll_script)

