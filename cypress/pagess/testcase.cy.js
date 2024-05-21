
import 'cypress-file-upload';
require('cypress-xpath');

class testCase {
    constructor() {
        this.elements = {
            // test case Btn
            test_case: () => cy.contains("Test Cases"),
            // Products Btn
            products_btn: () => cy.get("a[href='/products']"),
            //All products list 
            allproducts_text: () => cy.contains('All Products'),
            product1: () => cy.xpath("(//div[@class='product-overlay'])[1]"),
            product2: () => cy.xpath("(//div[@class='product-overlay'])[2]"),
            product3: () => cy.xpath("(//div[@class='product-overlay'])[3]"),
            // product view 1 
            product01: () => cy.get("a[href='/product_details/1']"),
            // Product details 
            product_title: () => cy.contains('Blue Top'),
            product_price: () => cy.contains('Rs. 500'),
            product_category: () => cy.contains('Category: Women > Tops'),
            product_availability: () => cy.contains('Availability:'),
            product_condition: () => cy.contains('Condition:'),
            product_brand: () => cy.contains('Brand:'),

        };
    }
    // Click BTN  test cases
    click_testcase() 
    {
        this.elements.test_case().click();
    };
    // Click btn products 
    click_products()
    {
        this.elements.products_btn().click();
    };
    // assertions 
    verify_products()
    {
        this.elements.allproducts_text().should('have.text', 'All Products');
        this.elements.product1().should('exist');
        this.elements.product2().should('exist');
        this.elements.product3().should('exist');
    };
    // select view product 1 
    clickview()
    {
        this.elements.product01().click();
    };
    // products details verification
    verify_details()
    {
        this.elements.product_title().should('be.visible')
        this.elements.product_brand().should('be.visible')
        this.elements.product_price().should('be.visible')
        this.elements.product_category().should('be.visible')
        this.elements.product_availability().should('be.visible')
        this.elements.product_condition().should('be.visible')
        this.elements.product_condition().should('be.visible')
    }

};

module.exports = new testCase();
