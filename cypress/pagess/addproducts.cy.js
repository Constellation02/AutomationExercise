
import 'cypress-file-upload';
require('cypress-xpath');

class addProducts {
    constructor() {
        this.elements = {
            // products btn
            products_btn: () => cy.get("a[href='/products']"),
            product01: () => cy.get('[data-product-id="1"]'),
            product02: () => cy.get('[data-product-id="2"]'),
            viewcart_btn: () => cy.contains("View Cart"),
            continue_shop: () => cy.contains("Continue Shopping"),
            bluetop: () => cy.contains('Blue Top'),
            mens_shirt: () => cy.contains('Men Tshirt'),
            price01: () => cy.contains('Rs. 500'),
            price02: () => cy.contains('Rs. 400'),
            total01: () => cy.get('tbody tr:nth-child(1) td:nth-child(5) p:nth-child(1)'),
            total02: () => cy.get('tbody tr:nth-child(2) td:nth-child(5) p:nth-child(1)'),
            quantity01:  () => cy.get('tbody tr:nth-child(1) td:nth-child(4) button:nth-child(1)'),
            quantity02:  () => cy.get('tbody tr:nth-child(2) td:nth-child(4) button:nth-child(1)'),
            view_product: () => cy.get("a[href='/product_details/3']"),
            incrise_quantity: () => cy.get("input[value='1']"),
            addtocart: () => cy.get("button[type='button']"),
            quantity03: () => cy.get('.disabled'),


        };
    }
    // click products btn
    btn_products()
    {
        this.elements.products_btn().click();
    }
    select_product01()
    {
        this.elements.product01().eq(0).click();
        this.elements.continue_shop().click();
        this.elements.product02().eq(0).click();
        this.elements.viewcart_btn().click();
    }
    // product assertion in the cart 
    products_present()
    {
        this.elements.bluetop().should('have.text', 'Blue Top');
        this.elements.mens_shirt().should('have.text', 'Men Tshirt'); 
        this.elements.price01().should('have.text', 'Rs. 500');
        this.elements.price02().should('have.text', 'Rs. 400');
        this.elements.total01().should('have.text', 'Rs. 500');
        this.elements.total02().should('have.text', 'Rs. 400');
        this.elements.quantity01().should('exist');
        this.elements.quantity02().should('exist'); 
    }
    // view product btn
    viewproduct(quantity)
    {
        this.elements.view_product().click();
        this.elements.incrise_quantity().clear().type(quantity)
        this.elements.addtocart().click()
        this.elements.viewcart_btn().click()
        this.elements.quantity03().should('eq', '4')
    }
};

module.exports = new addProducts();
