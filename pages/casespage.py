from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class CasesPage:
    def __init__(self, driver):
        self.driver = driver
        self.TEST_CASES_BTN = (By.XPATH, "(//a[@href='/test_cases'])[1]")

    
    def test_cases_btn(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.TEST_CASES_BTN)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: First btn sign up not found")
            return False