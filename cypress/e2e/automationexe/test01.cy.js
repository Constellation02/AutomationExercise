require('cypress-xpath');
import registerUser from '../../pagess/register_user.cy'



describe('Register User', () => {
    beforeEach (()=> {
        cy.visit('https://automationexercise.com/')
        
    });
    
    it('should load the homepage', () => {
        // Assert that the homepage is loaded successfully
        cy.url().should('eq', 'https://automationexercise.com/')
        registerUser.click_login_registerBtn()
        registerUser.verify_new_user_text()
        registerUser.enter_name("fabio")
        registerUser.enter_email("Testing_email@gmail.com")
        registerUser.click_create_acct()
        registerUser.click_gender()
        registerUser.enter_password("Welcome01")
        registerUser.selecting_date_of_birth('18', '8', '1998')
        registerUser.address_information("Fabio", "Armando", "Cybertron", "Dominican Republic", "Santo Domingo", "Santo Domingo Este", "Santo Domingo Nacional", "10001", "8095556767")
        registerUser.selectt_country('United States')
        registerUser.create_acct_Btn()
        registerUser.verify_created_text()
        registerUser.continiue_acct_Btn()
        //registerUser.click_delete_Btn()
        //registerUser.click_acct_delete_Btn()

    });
   
      
});