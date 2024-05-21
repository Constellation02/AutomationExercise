
require('cypress-xpath');

class loginUser {
    constructor() {
        this.elements = {
            // 'Signup / Login' button locator
            login_and_register_btn: () => cy.get("a[href='/login']"),
            // Verify 'Login to your account' text 
            login_text: () => cy.get("div[class='login-form'] h2"),
            // Email Address input locator & Password input locator
            enter_email: () => cy.get("input[data-qa='login-email']"),
            enter_password: () => cy.get("input[data-qa='login-password']"),
            // 'Login' button locator
            login_btn: () => cy.get("button[data-qa='login-button']"),
            // Logged in as text 
            Logged_in_text: () => cy.contains('Logged in as'),
            // Btn delete acct & acct deleted text
            delete_acct: () => cy.get("a[href='/delete_account']"),
            delete_text: () => cy.contains("Account Deleted!"),
            //email or password is incorrect! 
            loginfails: () => cy.contains("Your email or password is incorrect!"),
            //Logout Btn 
            logout_btn: () => cy.get("a[href='/logout']"),
            // Verify 'New User Signup!' text 
            newusersignup_text: () => cy.get("div[class='signup-form'] h2"),
            // Enter name and email address
            register_name: () => cy.xpath("//input[contains(@name,'name')]"),
            register_email: () => cy.xpath("//input[contains(@data-qa,'signup-email')]"),
            register_btn: () => cy.xpath("//button[contains(.,'Signup')]"),
            existing_email: () => cy.contains("Email Address already exist!")
        };
    }
    // Register user and email 
    enter_name(name, email) {
        this.elements.register_name().type(name);
        this.elements.register_email().type(email);
        this.elements.register_btn().click();
        this.elements.existing_email().should('have.text', 'Email Address already exist!')
    };
    // Verify 'New User Signup!' is visible
    verify_usersignup_text()
    {
        this.elements.newusersignup_text().should('have.text', 'New User Signup!')
    };
    // Click on Logout Btn
    click_LogoutBtn() 
    {
        this.elements.logout_btn().click();
    };
    // Click on 'Signup / Login' button
    click_login_registerBtn() 
    {
        this.elements.login_and_register_btn().click();
    };
    // Verify 'Login to your account' is visible
    verify_login_text()
    {
        this.elements.login_text().should('have.text', 'Login to your account')
    };
    // Enter name and email address
    input_login_credentials(email, password)
    {
        this.elements.enter_email().type(email);
        this.elements.enter_password().type(password);
    };
    // Click 'Login' button
    click_login_acct()
    {
        this.elements.login_btn().click();
    };
    verify_logged_text()
    {
        this.elements.Logged_in_text().should('have.text', 'Fabio Armando')
    };
    // Delete & Verify Account Deleted! is visible
    click_delete_Btn() 
    {
        this.elements.delete_acct().click();
    };
    verify_delete_text()
    {
        this.elements.delete_text().should('have.text', 'Account Deleted!')
    };
    unable_login()
    {
        this.elements.loginfails().should('have.text', 'Your email or password is incorrect!')
    };
};

module.exports = new loginUser();
