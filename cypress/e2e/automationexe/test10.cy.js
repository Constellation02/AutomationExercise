require('cypress-xpath');
import subCrition from '../../pagess/subcristion.cy'



describe(' Verify Subscription in home page', () => {
    beforeEach (()=> {
        cy.visit('https://automationexercise.com/')
        
    });
    
    it('Scroll down to footer and Verify text SUBSCRIPTION', () => {
        // Assert that the homepage is loaded successfully
        cy.url().should('eq', 'https://automationexercise.com/')
        subCrition.verify_subscrition();
        subCrition.input_email('testemail@gmail.com');
        
    });
   
      
});