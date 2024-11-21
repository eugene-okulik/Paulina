import requests
from endpoints.endpoint import Endpoint
from requests.exceptions import JSONDecodeError


class PatchObject(Endpoint):
    object_id = None

    def patch_new_object(self, object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f"{self.url}/{object_id}",
            json=payload,
            headers=headers
        )
        try:
            self.json = self.response.json()
            print(self.json)
        except JSONDecodeError:
            self.json = {'error': 'Response is not in JSON format'}

        if self.response.status_code == 200 and 'id' in self.json:
            self.object_id = self.json['id']
        else:
            self.object_id = None