import requests
from endpoints.endpoint import Endpoint
from requests.exceptions import JSONDecodeError


class GetObject(Endpoint):
    object_id = None

    def get_an_object(self, object_id):
        self.response = requests.get(f"{self.url}/{object_id}")
        try:
            self.json = self.response.json()
        except JSONDecodeError:
            self.json = {'error': 'Response is not in JSON format'}

        if self.response.status_code == 200:
            self.object_id = self.json.get('id')
            self.object_name = self.json.get('name')
            data = self.json.get('data', {})
            self.object_color = data.get('color')
            self.object_birthdate = data.get('birthdate')
            self.object_name_in_data = data.get('name')
            self.object_sex = data.get('sex')
            self.object_username = data.get('username')

        else:
            self.object_id = None
            self.object_name = None
            self.object_color = None
            self.object_birthdate = None
            self.object_name_in_data = None
            self.object_sex = None
            self.object_username = None
