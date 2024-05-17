require('cypress-xpath');
import loginUser from '../../pagess/login_user.cy'



describe('Logout User', () => {
    beforeEach (()=> {
        cy.visit('https://automationexercise.com/')
        
    });
    
    it('should be able to login and logout', () => {
        // Assert that the homepage is loaded successfully
        cy.url().should('eq', 'https://automationexercise.com/')
        loginUser.click_login_registerBtn()
        loginUser.verify_login_text()
        loginUser.input_login_credentials("TestingRep_email@gmail.com", "Welcome01")
        loginUser.click_login_acct()
        loginUser.click_LogoutBtn()
        cy.url().should('include', '/login');
        
        

    });
   
      
});