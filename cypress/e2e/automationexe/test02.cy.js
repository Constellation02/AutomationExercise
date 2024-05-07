require('cypress-xpath');
import loginUser from '../../pagess/login_user.cy'



describe('Login User with correct email and password', () => {
    beforeEach (()=> {
        cy.visit('https://automationexercise.com/')
        
    });
    
    it('should load the homepage & Login', () => {
        // Assert that the homepage is loaded successfully
        cy.url().should('eq', 'https://automationexercise.com/')
        loginUser.click_login_registerBtn()
        loginUser.verify_login_text()
        loginUser.input_login_credentials("Testing_email@gmail.com", "Welcome01")
        loginUser.click_login_acct()
        loginUser.click_delete_Btn()
        loginUser.verify_delete_text()

    });
   
      
});