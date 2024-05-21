require('cypress-xpath');
import testCase from '../../pagess/testcase.cy'



describe('Verify Test Cases Page', () => {
    beforeEach (()=> {
        cy.visit('https://automationexercise.com/')
        
    });
    
    it('should be able to navigate to test case page successfully', () => {
        // Assert that the homepage is loaded successfully
        cy.url().should('eq', 'https://automationexercise.com/')
        testCase.click_testcase()
        cy.url().should('include', '/test_cases');

        
    });
   
      
});