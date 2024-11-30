from locust import HttpUser, TaskSet, task


class CreateTaskSet(TaskSet):
    @task(1)
    def create_and_delete_object(self):
        payload = {
            "data": {
                "color": "Black",
                "birthdate": "2022-01-01",
                "name": "Larsik",
                "sex": "M",
                "username": "KotPerformance",
                "hobby": "Ohota",
                "work": "Rybalka",
                "education": "Vyshy Rybolovny Universitet imeni Leopolda",
                "distinctiveFeatures": "Dlinny usy i hvost",
                "mealPreferences": "Myshi",
                "size": "Ogromny",
                "weight": "Tyazholy"
            },
            "name": "Kot Bolshoi"
        }
        with self.client.post("/object", json=payload, catch_response=True) as response:
            if response.ok:
                object_id = response.json()['id']
                self.client.delete(f"/object/{object_id}")


class ReadTaskSet(TaskSet):
    @task(2)
    def create_read_delete_object(self):
        payload = {
            "data": {
                "color": "Red",
                "birthdate": "2022-01-01",
                "name": "Bonifacy",
                "sex": "M",
                "username": "KotBonifacyStary"
            },
            "name": "Kot Bonifacy"
        }
        with self.client.post("/object", json=payload, catch_response=True) as response:
            if response.ok:
                object_id = response.json()['id']
                self.client.get(f"/object/{object_id}")
                self.client.delete(f"/object/{object_id}")


class UpdateTaskSet(TaskSet):
    @task(1)
    def create_update_patch_delete_object(self):
        create_payload = {
            "data": {
                "color": "Red",
                "birthdate": "2022-01-01",
                "name": "Bonifacy",
                "sex": "M",
                "username": "KotBonifacyStary"
            },
            "name": "Kot Bonifacy"
        }
        with self.client.post("/object", json=create_payload, catch_response=True) as response:
            if response.ok:
                object_id = response.json()['id']

        update_payload = {
            "data": {
                "color": "RedUpdated",
                "birthdate": "2020-01-02",
                "name": "LeopoldUpdated",
                "sex": "M",
                "username": "KotLeopoldUpdated"
            },
            "name": "Kot Leopold Updated"
        }
        self.client.put(f"/object/{object_id}", json=update_payload)
        patch_payload = {
            "data": {
                "color": "RedPatched",
                "birthdate": "2020-02-02",
                "name": "KotPatched",
                "sex": "M",
                "username": "KotLeopoldPatched"
            }
        }
        self.client.patch(f"/object/{object_id}", json=patch_payload)
        self.client.delete(f"/object/{object_id}")


class APITestingUser(HttpUser):
    tasks = [CreateTaskSet, ReadTaskSet, UpdateTaskSet]
    min_wait = 1000
    max_wait = 3000
