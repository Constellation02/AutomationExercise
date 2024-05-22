require('cypress-xpath');
import addProducts from '../../pagess/addproducts.cy'



describe('Verify Subscription in Cart page', () => {
    beforeEach (()=> {
        cy.visit('https://automationexercise.com/')
        
    });
    
    it('Click Cart button and Verify text SUBSCRIPTION', () => {
        // Assert that the homepage is loaded successfully
        cy.url().should('eq', 'https://automationexercise.com/')
        addProducts.btn_products()
        addProducts.select_product01()
        addProducts.products_present()
        
        
    });
   
      
});