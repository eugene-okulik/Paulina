from test_ui_psivazhalezava_pw.pages.locators.create_account_locators import CreateAccountLocators as Loc
from test_ui_psivazhalezava_pw.pages.base_page import BasePage
from playwright.sync_api import expect


required_field_message_loc = '//input[contains(@class, "required-entry")]/following-sibling::div[@class="mage-error"]'

existing_email_message_loc = 'div[data-ui-id="message-error"] div[data-bind*="html: $parent.prepareMessageForHtml"]'

password_length_message_loc = 'div[id="password-error"]'


class CreateAccount(BasePage):
    page_url = '/customer/account/create/'

    def check_required_field_message(self, text):
        required_field_message = self.find(required_field_message_loc)
        expect(required_field_message).to_have_text(text)

    def check_existing_email_message(self, text):
        existing_email_message = self.find(existing_email_message_loc)
        expect(existing_email_message).to_have_text(text)

    def check_password_length_validation_message(self, text):
        password_length_validation_message = self.find(password_length_message_loc)
        expect(password_length_validation_message).to_have_text(text)

    def fill_create_account_form(self, firstname, lastname, email, password, confirm_password):
        firstname_field = self.find(Loc.firstname_field_loc)
        lastname_field = self.find(Loc.lastname_field_loc)
        email_field = self.find(Loc.email_field_loc)
        password_field = self.find(Loc.passw_field_loc)
        confirm_password_field = self.find(Loc.repeat_passw_field_loc)
        create_account_button = self.find(Loc.create_button_loc)
        firstname_field.fill(firstname)
        lastname_field.fill(lastname)
        email_field.fill(email)
        password_field.fill(password)
        confirm_password_field.fill(confirm_password)
        create_account_button.click()
