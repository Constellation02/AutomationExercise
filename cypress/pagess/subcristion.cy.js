
import 'cypress-file-upload';
require('cypress-xpath');

class subCrition {
    constructor() {
        this.elements = {
            // subscrition text in the footer
            subscrition_tex: () => cy.contains("Subscription"),
            //email input 
            email_input: () => cy.get("input[placeholder='Your email address']"),
            arrow_btn: () => cy.get("button[type='submit']"),
            email_assertion: () => cy.contains('You have been successfully subscribed!'),
            cart_btn: () => cy.get("header li:nth-child(3) a:nth-child(1)"),
            
        };
    }
 
    // assertions 
    verify_subscrition()
    {
        this.elements.subscrition_tex().should('have.text', "Subscription");
        this.elements.subscrition_tex().should('exist');
    };
    // input the email 
    input_email(email)
    {
        this.elements.email_input().type(email);
        this.elements.arrow_btn().click();
        this.elements.email_assertion().should('be.visible');
    }
    // Cart Btn 
    btn_cart()
    {
        this.elements.cart_btn().click();
    }
    
};

module.exports = new subCrition();
