import allure


class Endpoint:
    url = 'http://167.172.172.115:52353/object'
    response = None
    json = None
    headers = {'Content-type': 'application/json'}
    object_id = None
    object_name = None
    object_color = None
    object_birthdate = None
    object_name_in_data = None
    object_sex = None
    object_username = None

    @allure.step("Verify response status code is 200")
    def check_that_status_code_is_200(self):
        assert self.response.status_code == 200, 'Status code is incorrect for valid data'

    @allure.step("Verify response status code is 400")
    def check_that_status_code_is_400(self):
        assert self.response.status_code == 400, 'Status code is incorrect for invalid data'

    @allure.step("Verify response status code is 404")
    def check_that_status_code_is_404(self):
        assert self.response.status_code == 404, 'Status code is incorrect for not present data'

    @allure.step("Verify response 'id' is correct")
    def check_that_id_is_correct(self, expected_id):
        assert self.object_id == expected_id, 'Id is incorrect'

    @allure.step("Verify response 'name' is correct")
    def check_that_name_is_correct(self, expected_name):
        assert self.object_name == expected_name, 'Name is incorrect'

    @allure.step("Verify response 'color' is correct")
    def check_that_color_is_correct(self, expected_color):
        assert self.object_color == expected_color, 'Color is incorrect'

    @allure.step("Verify response 'birthdate' is correct")
    def check_that_birthdate_is_correct(self, expected_birthdate):
        assert self.object_birthdate == expected_birthdate, 'Birth date is incorrect'

    @allure.step("Verify response 'name' in 'data' is correct")
    def check_that_name_in_data_is_correct(self, expected_name_in_data):
        assert self.object_name_in_data == expected_name_in_data, 'Name in data is incorrect'

    @allure.step("Verify response 'sex' is correct")
    def check_that_sex_is_correct(self, expected_sex):
        assert self.object_sex == expected_sex, 'Sex is incorrect'

    @allure.step("Verify response 'username' is correct")
    def check_that_username_is_correct(self, expected_username):
        assert self.object_username == expected_username, 'Username is incorrect'
