from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import Select




class Category: 
    def __init__(self, driver):
        self.driver = driver 
        self.WOMEN = (By.XPATH, "//a[@href='#Women']")
        self.DRESS = (By.XPATH, "//a[@href='/category_products/1']")
        self.WOMEN_DRESS_TEXT = (By.XPATH, "//h2[@class='title text-center'][contains(.,'Women - Dress Products')]")
        self.MEN = (By.XPATH, "//a[@href='#Men']")
        self.JEANS = (By.XPATH, "//a[@href='/category_products/6']")
        self.MEN_JEANS_TEXT = (By.XPATH, "//h2[@class='title text-center'][contains(.,'Men - Jeans Products')]")


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