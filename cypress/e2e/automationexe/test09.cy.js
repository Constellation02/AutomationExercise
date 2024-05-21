require('cypress-xpath');
import testCase from '../../pagess/testcase.cy'



describe('Search Product', () => {
    beforeEach (()=> {
        cy.visit('https://automationexercise.com/')
        
    });
    
    it('should be able to navigate to All products page successfully', () => {
        // Assert that the homepage is loaded successfully
        cy.url().should('eq', 'https://automationexercise.com/')
        testCase.click_products()
        cy.url().should('include', '/products');
        testCase.verify_products();
        testCase.search_type('Frozen Tops For Kids');
        testCase.searched_producttext();
        
    });
   
      
});