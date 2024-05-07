

require('cypress-xpath');

class loginUser {
    constructor() {
        this.elements = {
            // 'Signup / Login' button locator
            login_and_register_btn: () => cy.get("a[href='/login']"),
            // Verify 'Login to your account' locator 
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
            loginfails: () => cy.contains("Your email or password is incorrect!")
        };
    }
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
        this.elements.Logged_in_text().should('have.text', 'Logged in as  fabio')
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
