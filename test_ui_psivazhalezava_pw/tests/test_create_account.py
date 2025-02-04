import pytest


@pytest.mark.parametrize("firstname,lastname,email,password,confirm_password", [
    ("", "Sery", "jane.doe@example.com", "Password456", "Password456"),
    ("Kat", "", "jane.doe@example.com", "password123", "password123")
])
def test_create_account_negative_empty_names(create_new_account_page, firstname, lastname, email, password,
                                             confirm_password):
    create_new_account_page.open_page()
    create_new_account_page.fill_create_account_form(firstname, lastname, email, password, confirm_password)
    create_new_account_page.check_required_field_message(text='This is a required field.')


def test_check_existing_email_message(create_new_account_page):
    create_new_account_page.open_page()
    create_new_account_page.fill_create_account_form("Kot", "Chorny", "johndoe@domain.com", "Qwerty123", "Qwerty123")
    create_new_account_page.check_existing_email_message(text='There is already an account with this email address. '
                                                              'If you are sure that it is your email address, '
                                                              'click here to get your password and access your account.'
                                                              '')


def test_check_password_length_validation_message(create_new_account_page):
    create_new_account_page.open_page()
    create_new_account_page.fill_create_account_form("Kot", "Chorny", "johndoe2@domain.com", "qwertyu", "qwertyu")
    create_new_account_page.check_password_length_validation_message('Minimum length of this field '
                                                                     'must be equal or greater than 8 symbols. '
                                                                     'Leading and trailing spaces will be ignored.')
