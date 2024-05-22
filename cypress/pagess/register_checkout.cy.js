
import 'cypress-file-upload';
require('cypress-xpath');

class checkout {
    constructor() {
        this.elements = {
            // adding product to the cart 
            product01: () => cy.get('[data-product-id="1"]'),
            product02: () => cy.get('[data-product-id="2"]'),
            viewcart_btn: () => cy.contains("View Cart"),
            continue_shop: () => cy.contains("Continue Shopping"),
            procedtocheckout: () => cy.get('.btn.btn-default.check_out'),
            register: () => cy.contains('u', 'Register / Login'),
            register0: () => cy.get("a[href='/login']"),
            name: () => cy.get("input[placeholder='Name']"),
            email: () => cy.get("input[data-qa='signup-email']"),
            signup_btn: () => cy.get("button[data-qa='signup-button']"),
            mrs: () => cy.get("input[value='Mrs']"),
            password: () => cy.get("input[type='password']"),
            days: () => cy.get("select[data-qa='days']"),
            months: () => cy.get("select[data-qa='months']"),
            years: () => cy.get("select[data-qa='years']"),
            newsletter: () => cy.get('#newsletter'),
            specialoffer: () => cy.get('#optin'),
            // adress information locators 
            firstname: () => cy.get("input[data-qa='first_name']"),
            lastname: () => cy.get("input[data-qa='last_name']"),
            company: () => cy.get("input[data-qa='company']"),
            address: () => cy.get("input[data-qa='address']"),
            address2: () => cy.get('input[data-qa="address2"]'),
            country: () => cy.get("select[data-qa='country']"),
            state: () => cy.get("input[data-qa='state']"),
            city: () => cy.get("input[data-qa='city']"),
            zipcode: () => cy.get("input[data-qa='zipcode']"),
            mobilenumber: () => cy.get("input[data-qa='mobile_number']"),
            create_acct: () => cy.get("button[data-qa='create-account']"),
            // proccess 
            acct_createdtext: () => cy.contains('Account Created!'),
            continue_btn: () => cy.contains('Continue'),
            cart_btn: () => cy.get("a[href='/view_cart']"),
            checkoutproced: () => cy.contains('Proceed To Checkout'),
            placeorder: () => cy.get('a[href="/payment"]'),
            nameoncard: () => cy.get('input[data-qa="name-on-card"]'),
            cardnumber: () => cy.get('input[data-qa="card-number"]'),
            cvc: () => cy.get('input[data-qa="cvc"]'),
            expirationmonth: () => cy.get('input[data-qa="expiry-month"]'),
            expirationyear: () => cy.get('input[data-qa="expiry-year"]'),
            pay: () => cy.get(".form-control.btn.btn-primary.submit-button"),
            payconfirmation: () => cy.contains('Your order has been placed successfully!'),
            orderplaced: () => cy.contains('Order Placed!'),
            delete_acct: () => cy.get("a[href='/delete_account']"),
            deleted_text: () => cy.contains('Account Deleted!'),
            //login credentials 
            emai_address: () => cy.get("input[data-qa='login-email']"),
            password_input: () => cy.get("input[placeholder='Password']"),
            login_btn: () => cy.get("button[data-qa='login-button']"),


            
        };
    }
    // login
    login(emial, pass)
    {
        this.elements.emai_address().type(emial)
        this.elements.password_input().type(pass)
        this.elements.login_btn().click()
    }
    // Btn click register 
    clickregister()
    {
        this.elements.register0().click();
    }
    select_product01()
    {
        this.elements.product01().eq(0).click();
        this.elements.continue_shop().click();
        this.elements.product02().eq(0).click();
        this.elements.viewcart_btn().click();
        cy.url().should('include', '/view_cart')
        this.elements.procedtocheckout().click();
        this.elements.register().eq(0).click(); 
    }
    signup01(name, email)
    {
        this.elements.name().type(name);
        this.elements.email().type(email);
        this.elements.signup_btn().click();
    }
    information(pass)
    {
        this.elements.mrs().click();
        this.elements.password().type(pass)
        this.elements.days().select('18')
        this.elements.months().select('8')
        this.elements.years().select('1998')
        this.elements.newsletter().check()
        this.elements.specialoffer().check()
        cy.get('#newsletter').should('be.checked');
        cy.get('#optin').should('be.checked');
    }
    // Adress information
    address_information(name, lastname, company, address, address2, state, city, zipcode, mobilenumber)
    {
        this.elements.firstname().type(name)
        this.elements.lastname().type(lastname)
        this.elements.company().type(company)
        this.elements.address().type(address)
        this.elements.address2().type(address2)
        this.elements.country().select('United States')
        this.elements.state().type(state)
        this.elements.city().type(city)
        this.elements.zipcode().type(zipcode)
        this.elements.mobilenumber().type(mobilenumber)
        this.elements.create_acct().click()
    }
    // fishing the transaction 
    transaction(card, number, cvc, expirationmonth, expirationyear )
    {
        this.elements.acct_createdtext().should('have.text', 'Account Created!')
        this.elements.continue_btn().click()
        this.elements.cart_btn().eq(0).click()
        this.elements.checkoutproced().click()
        this.elements.placeorder().click()
        this.elements.nameoncard().type(card)
        this.elements.cardnumber().type(number)
        this.elements.cvc().type(cvc)
        this.elements.expirationmonth().type(expirationmonth)
        this.elements.expirationyear().type(expirationyear)
        this.elements.pay().click()
        this.elements.payconfirmation().should('exist')
        this.elements.orderplaced().should('have.text', 'Order Placed!')
        this.elements.delete_acct().click()
        this.elements.deleted_text().should('have.text', 'Account Deleted!')
        this.elements.continue_btn().click()
    }
    // test 15 transaction 
    transaction15(card, number, cvc, expirationmonth, expirationyear)
    {
        this.elements.acct_createdtext().should('have.text', 'Account Created!')
        this.elements.continue_btn().click()
        this.elements.product01().eq(0).click();
        this.elements.continue_shop().click();
        this.elements.product02().eq(0).click();
        this.elements.viewcart_btn().click();
        cy.url().should('include', '/view_cart')
        this.elements.procedtocheckout().click();
        this.elements.placeorder().click()
        this.elements.nameoncard().type(card)
        this.elements.cardnumber().type(number)
        this.elements.cvc().type(cvc)
        this.elements.expirationmonth().type(expirationmonth)
        this.elements.expirationyear().type(expirationyear)
        this.elements.pay().click()
        this.elements.orderplaced().should('have.text', 'Order Placed!')
        this.elements.delete_acct().click()
        this.elements.deleted_text().should('have.text', 'Account Deleted!')
        this.elements.continue_btn().click()
    }
    // test 16 transaction
    transaction16(card, number, cvc, expirationmonth, expirationyear)
    {
        this.elements.product01().eq(0).click();
        this.elements.continue_shop().click();
        this.elements.product02().eq(0).click();
        this.elements.viewcart_btn().click();
        cy.url().should('include', '/view_cart')
        this.elements.procedtocheckout().click();
        this.elements.placeorder().click()
        this.elements.nameoncard().type(card)
        this.elements.cardnumber().type(number)
        this.elements.cvc().type(cvc)
        this.elements.expirationmonth().type(expirationmonth)
        this.elements.expirationyear().type(expirationyear)
        this.elements.pay().click()
        this.elements.orderplaced().should('have.text', 'Order Placed!')
        this.elements.delete_acct().click()
        this.elements.deleted_text().should('have.text', 'Account Deleted!')
        this.elements.continue_btn().click()
    }

};

module.exports = new checkout();
