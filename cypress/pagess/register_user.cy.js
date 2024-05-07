

require('cypress-xpath');

class registerUser {
    constructor() {
        this.elements = {
            // Click on 'Signup / Login' button
            login_and_register_btn: () => cy.contains('Signup / Login'),
            // Verify 'New User Signup!' is visible
            new_user_text: () => cy.contains('New User Signup!'),
            // Enter name and email address
            register_name: () => cy.xpath("//input[contains(@name,'name')]"),
            register_email: () => cy.xpath("//input[contains(@data-qa,'signup-email')]"),
            // Click 'Signup' button
            register_btn: () => cy.xpath("//button[contains(.,'Signup')]"),
            // Title button
            gender2_btn: () => cy.xpath("//input[contains(@id,'gender2')]"),
            //Password input 
            password_input: () => cy.xpath("//input[contains(@id,'password')]"),
            //selecting Date of Birth 
            select_days: () => cy.xpath("//select[contains(@id,'days')]"),
            select_months: () => cy.xpath("//select[contains(@id,'months')]"),
            select_years: () => cy.xpath("//select[contains(@id,'years')]"),
            //Sign up for newsletter and receive special offers
            newsletter_btn: () => cy.xpath("//input[contains(@id,'newsletter')]"),
            special_btn: () => cy.xpath("//input[contains(@id,'optin')]"),
            //Address information
            first_name: () => cy.xpath("//input[contains(@id,'first_name')]"),
            last_name: () => cy.xpath("//input[contains(@id,'last_name')]"),
            company: () => cy.xpath("//input[contains(@id,'company')]"),
            address1: () => cy.xpath("//input[contains(@id,'address1')]"),
            address2: () => cy.xpath("//input[contains(@id,'address2')]"),
            select_country: () => cy.xpath("//select[contains(@id,'country')]"),
            state: () => cy.xpath("//input[contains(@id,'state')]"),
            city: () => cy.xpath("//input[contains(@id,'city')]"),
            zipcode: () => cy.xpath("//input[contains(@id,'zipcode')]"),
            mobile_number: () => cy.xpath("//input[contains(@id,'mobile_number')]"),
            //Create Account Btn
            create_acct: () => cy.get('button[data-qa="create-account"]'),
            // Verify Account Created! is visible
            acct_created_text: () => cy.xpath("//b[contains(.,'Account Created!')]"),
            continue_acct_btn: () => cy.xpath("//a[@href='/'][contains(.,'Continue')]"),
            // Delete & Verify Account Deleted! is visible
            delete_acct: () => cy.xpath("//a[contains(@href,'account')]"),
            acct_deleted_text: () => cy.xpath("//b[contains(.,'Account Deleted!')]"),
            //Continue Btn
            acct_deleted_continue: () => cy.xpath("//a[@href='/'][contains(.,'Continue')]")
        };
    }

    click_login_registerBtn() {
        this.elements.login_and_register_btn().click();
    };

    enter_name(name) {
        this.elements.register_name().type(name);
    };

    enter_email(email) {
        this.elements.register_email().type(email);
    };

    click_create_acct() {
        this.elements.register_btn().click();
    };
    verify_new_user_text(){
        this.elements.new_user_text().should('have.text', 'New User Signup!')
    };

    click_gender() {
        this.elements.gender2_btn().click();
    };
    enter_password(password) {
        this.elements.password_input().type(password);
    };
    selecting_date_of_birth(days, months, year){
        this.elements.select_days().select(days)
        this.elements.select_months().select(months)
        this.elements.select_years().select(year)
    };
    special_newsletter_btn(){
        this.elements.newsletter_btn().click();
        this.elements.special_btn().click();
    };
    address_information(name, lastname, company, address, address2, state, city, zip, number){
        this.elements.first_name().type(name)
        this.elements.last_name().type(lastname)
        this.elements.company().type(company)
        this.elements.address1().type(address)
        this.elements.address2().type(address2)
        this.elements.state().type(state)
        this.elements.city().type(city)
        this.elements.zipcode().type(zip)
        this.elements.mobile_number().type(number)

    };
    selectt_country(country){
        this.elements.select_country().select(country)

    };
    create_acct_Btn() {
        this.elements.create_acct().click();
    };
    verify_created_text(){
        this.elements.acct_created_text().should('have.text', 'Account Created!')
    };
    continiue_acct_Btn() {
        this.elements.continue_acct_btn().click();
    };
    click_delete_Btn() {
        this.elements.delete_acct().click();
    };
    verify_delete_text(){
        this.elements.acct_deleted_text().should('have.text', 'Account Deleted!')
    };
    click_acct_delete_Btn() {
        this.elements.acct_deleted_continue().click();
    };
    
};

module.exports = new registerUser();
