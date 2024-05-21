require('cypress-xpath');
import subCrition from '../../pagess/subcristion.cy'



describe('Verify Subscription in Cart page', () => {
    beforeEach (()=> {
        cy.visit('https://automationexercise.com/')
        
    });
    
    it('Click Cart button and Verify text SUBSCRIPTION', () => {
        // Assert that the homepage is loaded successfully
        cy.url().should('eq', 'https://automationexercise.com/')
        subCrition.btn_cart()
        subCrition.verify_subscrition();
        subCrition.input_email('testemail@gmail.com');
        
    });
   
      
});