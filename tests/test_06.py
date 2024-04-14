import unittest
from selenium import webdriver
from pages.contactus import ContactForm
import time 


class ContactUsDemo(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://automationexercise.com')
        self.driver.maximize_window()
        print("page loaded")


    def test_contactus(self):
        login_page = ContactForm(self.driver)
        login_page.contactus()
        login_page.get_in_touch()
        print("Assertion passed: 'GET IN TOUCH' text is visible")
        login_page.name("Fabio")
        login_page.email("Laparatuya1@gmail.com")
        login_page.subject("this is a tests")
        login_page.message("This is a message for testing")
        login_page.upload_file("C:/Users/fabio/OneDrive/Documentos/savepicture/IMG_8517.jpeg")
        login_page.submit()
        login_page.handle_alert()
        login_page.success_message()
        print("Assertion passed: 'Success! Your details have been submitted successfully.")
        login_page.home()
        print("Logged out, Current URL:", self.driver.current_url)
        time.sleep(10)



    def tearDown(self):
        self.driver.quit()