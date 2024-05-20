require('cypress-xpath');
import loginUser from '../../pagess/login_user.cy'



describe('Register User with existing email', () => {
    beforeEach (()=> {
        cy.visit('https://automationexercise.com/')
        
    });
    
    it('should be display Email Address already exist!', () => {
        // Assert that the homepage is loaded successfully
        cy.url().should('eq', 'https://automationexercise.com/')
        loginUser.click_login_registerBtn()
        loginUser.verify_usersignup_text()
        loginUser.enter_name('Fabio','TestingRep_email@gmail.com')

        
        
        

    });
   
      
});