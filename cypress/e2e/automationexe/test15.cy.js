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
        checkout.signup01('Fabio', 'testin_fa0068biog@gmail.com')
        checkout.information('Welcome01')
        checkout.address_information('Fabio', 'Armando', 'Tesla', 'Miami', 'Mar A Lago', 'Florida', 'Boca raton', '11001', '4736698521')
        checkout.transaction15('Fabio Armando', '00010000001001', '311', '08', '2024')
        
        
        
    });
   
      
});