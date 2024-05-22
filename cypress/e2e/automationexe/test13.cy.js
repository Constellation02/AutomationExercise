require('cypress-xpath');
import addProducts from '../../pagess/addproducts.cy'



describe('Verify Product quantity in Cart', () => {
    beforeEach (()=> {
        cy.visit('https://automationexercise.com/')
        
    });
    
    it('Click Cart button and Verify Product quantity in Cart', () => {
        // Assert that the homepage is loaded successfully
        cy.url().should('eq', 'https://automationexercise.com/')
        addProducts.btn_products()
        addProducts.viewproduct('4')
        
        
        
    });
   
      
});