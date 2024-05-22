require('cypress-xpath');
import checkout from '../../pagess/register_checkout.cy'



describe('Place Order: Register while Checkout', () => {
    beforeEach (()=> {
        cy.visit('https://automationexercise.com/')
        
    });
    
    it('Register while Checkout', () => {
        // Assert that the homepage is loaded successfully
        cy.url().should('eq', 'https://automationexercise.com/')
        checkout.clickregister()
        checkout.login('testin_fabiog@gmail.com', 'Welcome01')
        checkout.transaction16('Fabio Armando', '00010000001001', '311', '08', '2024')
        
        
        
    });
   
      
});