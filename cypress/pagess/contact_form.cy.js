
import 'cypress-file-upload';
require('cypress-xpath');

class contactForm {
    constructor() {
        this.elements = {
            //Contact Us BTN
            contact_us: () => cy.get("a[href='/contact_us']"),
            //Get in touch
            name: () => cy.get("input[placeholder='Name']"),
            email: () => cy.get("input[placeholder='Email']"),
            subject: () => cy.get("input[placeholder='Subject']"),
            message_here: () => cy.get('#message'),
            // Submit BTN
            submit_btn: () => cy.get("input[value='Submit']"),
            // Success message 
            success_message: () => cy.contains('Success! Your details have been submitted successfully.'),
            // Btn Home 
            home_btn: () => cy.contains('Home'),

        };
    }
    // Click BTN  contact Us
    click_contactform() 
    {
        this.elements.contact_us().click();
    };
    // fill up the get in touch form 
    enter_form(name, email, subject, messsage) 
    {
        this.elements.name().type(name);
        this.elements.email().type(email);
        this.elements.subject().type(subject);
        this.elements.message_here().type(messsage);
    };
    // Upload the file 
    upload_file()
    {
        const fileName = 'test.jpg';
        cy.get("input[type='file']").attachFile(fileName);
    };
    // Btn to submit 
    btn_submit()
    {
        this.elements.submit_btn().click()
    };
    // Verify success message 
    verify_success_message()
    {
        this.elements.success_message().should('have.text', 'Success! Your details have been submitted successfully.')
    };
    // Btn go Home
    btn_home()
    {
        this.elements.home_btn().click()
    }

};

module.exports = new contactForm();
