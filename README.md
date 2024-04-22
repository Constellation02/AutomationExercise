# :gem: Automation Exercise - Automated GUI Testing

## :teacher: About this project
The project was created to practice test automation skills using the Selenium (python) POM framework, utilizing my skills learned. The website under test is a website specifically designed for automated testing. The project contains a total of 26 automated tests, created based on test cases defined by the site's developers. After running and executing the tests, using the proper command, a test report can be generated, which describes in detail the activities performed and the statuses of each test.

## :wrench: Tools:
+ Vs code
+ pytest 
+ Selenium WebDriver
+ pytest-html

## :art: Project Design:
+ Page Object Model
+ Data-Driven approach
+ Behavior-Driven approach

## :warning: Note:
The tests have been run in Chrome in private mode, which blocks ads. However, it is possible that the test may not work in other browsers due to pop-up ads that require closing.
Tests are not always stable, because sometimes the ads are not blocked completely for some reason.

In order to generate Report:
* Commandline: 
` python -m pytest -v --html=reports/report.html `

* Just run all the test: 
` python -m `

* Just run one test: 
` pytest tests\test_03.py `

## :100: The project includes all available test cases:
### :white_check_mark: Test Case 1: Register User
<ol> 1. Launch browser </ol>
<ol> 2. Navigate to url 'http://automationexercise.com' </ol>
<ol> 3. Verify that home page is visible successfully </ol>
<ol> 4. Click on 'Signup / Login' button </ol>
<ol> 5. Verify 'New User Signup!' is visible </ol>
<ol> 6. Enter name and email address </ol>
<ol> 7. Click 'Signup' button </ol>
<ol> 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible </ol>
<ol> 9. Fill details: Title, Name, Email, Password, Date of birth </ol>
<ol> 10. Select checkbox 'Sign up for our newsletter!' </ol>
<ol> 11. Select checkbox 'Receive special offers from our partners!' </ol>
<ol> 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number </ol>
<ol> 13. Click 'Create Account button' </ol>
<ol> 14. Verify that 'ACCOUNT CREATED!' is visible </ol>
<ol> 15. Click 'Continue' button </ol>
<ol> 16. Verify that 'Logged in as username' is visible </ol>
<ol> 17. Click 'Delete Account' button </ol>
<ol> 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button </ol>

---

### :white_check_mark: Test Case 2: Login User with correct email and password
<ol> 1. Launch browser </ol>
<ol> 2. Navigate to url 'http://automationexercise.com' </ol>
<ol> 3. Verify that home page is visible successfully </ol>
<ol> 4. Click on 'Signup / Login' button </ol>
<ol> 5. Verify 'Login to your account' is visible </ol>
<ol> 6. Enter correct email address and password </ol>
<ol> 7. Click 'login' button </ol>
<ol> 8. Verify that 'Logged in as username' is visible </ol>

---

### :white_check_mark: Test Case 3: Login User with incorrect email and password
<ol> 1. Launch browser </ol>
<ol> 2. Navigate to url 'http://automationexercise.com' </ol>
<ol> 3. Verify that home page is visible successfully </ol>
<ol> 4. Click on 'Signup / Login' button </ol>
<ol> 5. Verify 'Login to your account' is visible </ol>
<ol> 6. Enter incorrect email address and password </ol>
<ol> 7. Click 'login' button </ol>
<ol> 8. Verify error 'Your email or password is incorrect!' is visible </ol>

---

### :white_check_mark: Test Case 4: Logout User
<ol> 1. Launch browser </ol>
<ol> 2. Navigate to url 'http://automationexercise.com' </ol>
<ol> 3. Verify that home page is visible successfully </ol>
<ol> 4. Click on 'Signup / Login' button </ol>
<ol> 5. Verify 'Login to your account' is visible </ol>
<ol> 6. Enter correct email address and password </ol>
<ol> 7. Click 'login' button </ol>
<ol> 8. Verify that 'Logged in as username' is visible </ol>
<ol> 9. Click 'Logout' button </ol>
<ol> 10. Verify that user is navigated to login page </ol>

---

### :white_check_mark: Test Case 5: Register User with existing email
<ol> 1. Launch browser </ol>
<ol> 2. Navigate to url 'http://automationexercise.com' </ol>
<ol> 3. Verify that home page is visible successfully </ol>
<ol> 4. Click on 'Signup / Login' button </ol>
<ol> 5. Verify 'New User Signup!' is visible </ol>
<ol> 6. Enter name and already registered email address </ol>
<ol> 7. Click 'Signup' button </ol>
<ol> 8. Verify error 'Email Address already exist!' is visible </ol>

---

### :white_check_mark: Test Case 6: Contact Us Form
<ol> 1. Launch browser </ol>
<ol> 2. Navigate to url 'http://automationexercise.com' </ol>
<ol> 3. Verify that home page is visible successfully </ol>
<ol> 4. Click on 'Contact Us' button </ol>
<ol> 5. Verify 'GET IN TOUCH' is visible </ol>
<ol> 6. Enter name, email, subject and message </ol>
<ol> 7. Upload file </ol>
<ol> 8. Click 'Submit' button </ol>
<ol> 9. Click OK button </ol>
<ol> 10. Verify success message 'Success! Your details have been submitted successfully.' is visible </ol>
<ol> 11. Click 'Home' button and verify that landed to home page successfully </ol>

---

### :white_check_mark: Test Case 7: Verify Test Cases Page
<ol> 1. Launch browser </ol>
<ol> 2. Navigate to url 'http://automationexercise.com' </ol>
<ol> 3. Verify that home page is visible successfully </ol>
<ol> 4. Click on 'Test Cases' button </ol>
<ol> 5. Verify user is navigated to test cases page successfully </ol>

---

### :white_check_mark: Test Case 8: Verify All Products and product detail page
<ol> 1. Launch browser </ol>
<ol> 2. Navigate to url 'http://automationexercise.com' </ol>
<ol> 3. Verify that home page is visible successfully </ol>
<ol> 4. Click on 'Products' button </ol>
<ol> 5. Verify user is navigated to ALL PRODUCTS page successfully </ol>
<ol> 6. The products list is visible </ol>
<ol> 7. Click on 'View Product' of first product </ol>
<ol> 8. User is landed to product detail page </ol>
<ol> 9. Verify that detail detail is visible: product name, category, price, availability, condition, brand </ol>

---

### :white_check_mark: Test Case 9: Search Product
<ol> 1. Launch browser </ol>
<ol> 2. Navigate to url 'http://automationexercise.com' </ol>
<ol> 3. Verify that home page is visible successfully </ol>
<ol> 4. Click on 'Products' button </ol>
<ol> 5. Verify user is navigated to ALL PRODUCTS page successfully </ol>
<ol> 6. Enter product name in search input and click search button </ol>
<ol> 7. Verify 'SEARCHED PRODUCTS' is visible </ol>
<ol> 8. Verify all the products related to search are visible </ol>
