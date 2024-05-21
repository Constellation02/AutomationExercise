require('cypress-xpath');
import contactForm from '../../pagess/contact_form.cy'



describe('Contact Us Form', () => {
    beforeEach (()=> {
        cy.visit('https://automationexercise.com/')
        
    });
    
    it('should be able to fill up a contact form and navigate to home page', () => {
        // Assert that the homepage is loaded successfully
        cy.url().should('eq', 'https://automationexercise.com/')
        contactForm.click_contactform()
        contactForm.enter_form('Fabio', 'testing_email@testing.com', 'This is a test', 'I love testing')
        contactForm.upload_file()
        contactForm.btn_submit()
        contactForm.verify_success_message()
        contactForm.btn_home()
        cy.url().should('eq', 'https://automationexercise.com/')
    });
   
      
});