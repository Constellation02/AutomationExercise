
import 'cypress-file-upload';
require('cypress-xpath');

class testCase {
    constructor() {
        this.elements = {
            // test case Btn
            test_case: () => cy.contains("Test Cases")
        };
    }
    // Click BTN  test cases
    click_testcase() 
    {
        this.elements.test_case().click();
    };
    

};

module.exports = new testCase();
