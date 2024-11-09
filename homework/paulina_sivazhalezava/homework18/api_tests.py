import requests


def test_one_object():
    created_object = new_object()
    object_id = created_object['id']
    response = requests.get(f'http://167.172.172.115:52353/object/{object_id}').json()
    assert response['id'] == object_id, "id does not match"
    assert response['name'] == created_object['name'], "Name does not match"
    assert response['data']['color'] == created_object['data']['color'], "Color does not match"
    assert response['data']['birthdate'] == created_object['data']['birthdate'], "Birthdate does not match"
    assert response['data']['name'] == created_object['data']['name'], "Name in data does not match"
    assert response['data']['sex'] == created_object['data']['sex'], "sex does not match"
    assert response['data']['username'] == created_object['data']['username'], "Username does not match"
    cleanup(object_id)


def cleanup(object_id):
    requests.delete(f'http://167.172.172.115:52353/object/{object_id}')


def test_post_an_object_positive():
    body = {
        "data": {
            "color": "Grey",
            "birthdate": "2023-01-01",
            "name": "Kot",
            "sex": "M",
            "username": "KotSuslik"
        },
        "name": "Kot Sery"
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )

    assert response.status_code == 200, 'Status code is incorrect'
    response_data = response.json()
    assert 'name' in response.json(), "Response does not have 'name' attribute"
    assert isinstance(response.json()['name'], str), "'name' should be a string"
    assert 'id' in response.json(), "Response does not have 'id' attribute"
    assert 'data' in response.json(), "Response does not contain 'data'"
    assert isinstance(response.json()['data'], dict), "'data' should be an object"
    object_id = response_data['id']
    cleanup(object_id)


def test_post_an_object_negative():
    body_missing_data = {
        "name": "Kot Sery"
    }

    headers = {'Content-Type': 'application/json'}
    response_missing_data = requests.post(
        'http://167.172.172.115:52353/object',
        json=body_missing_data,
        headers=headers
    )

    assert response_missing_data.status_code == 400, 'Status code is incorrect for missing data'
    body_missing_name = {
        "data": {
            "color": "Grey",
            "birthdate": "2023-01-01",
            "name": "Kot",
            "sex": "M",
            "username": "KotSuslik"
        }
    }
    response_missing_name = requests.post(
        'http://167.172.172.115:52353/object',
        json=body_missing_name,
        headers=headers
    )
    assert response_missing_name.status_code == 400, 'Status code is incorrect for missing name'
    body_invalid_name = {
        "data": {
            "color": "Grey",
            "birthdate": "2023-01-01",
            "name": "Kot",
            "sex": "M",
            "username": "KotSuslik"
        },
        "name": 1234
    }
    response_invalid_name = requests.post(
        'http://167.172.172.115:52353/object',
        json=body_invalid_name,
        headers=headers
    )
    assert response_invalid_name.status_code == 400, 'Status code is incorrect for invalid name'
    body_invalid_data = {
        "data": [{
            "color": "Grey",
            "birthdate": "2023-01-01",
            "name": "Kot",
            "sex": "M",
            "username": "KotSuslik"
        }],
        "name": "Lopata"
    }
    response_invalid_data = requests.post(
        'http://167.172.172.115:52353/object',
        json=body_invalid_data,
        headers=headers
    )
    assert response_invalid_data.status_code == 400, 'Status code is incorrect for invalid data'


def new_object():
    body = {
        "data": {
            "color": "White",
            "birthdate": "2023-01-01",
            "name": "Kot",
            "sex": "M",
            "username": "KotSuslik"
        },
        "name": "Kot Bely"
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    return response.json()


def test_update_an_object_positive():
    created_object = new_object()
    object_id = created_object['id']
    update_body = {
        "data": {
            "birthdate": "2024-01-01",
            "color": "GreyUpdated",
            "name": "KotUpdated",
            "sex": "MUpdated",
            "username": "KotSuslikUpdated"
        },
        "name": "KotUpdated2"
    }
    headers = {'Content-Type': 'application/json'}
    requests.put(f'http://167.172.172.115:52353/object/{object_id}',
                 json=update_body, headers=headers).json()
    response = requests.get(f'http://167.172.172.115:52353/object/{object_id}').json()
    assert str(response['id']) == str(object_id), "id does not match"
    assert response['name'] == update_body['name'], "Name does not match"
    assert response['data']['color'] == update_body['data']['color'], "Color does not match"
    assert response['data']['birthdate'] == update_body['data']['birthdate'], "Birthdate does not match"
    assert response['data']['name'] == update_body['data']['name'], "Name in data does not match"
    assert response['data']['sex'] == update_body['data']['sex'], "Sex does not match"
    assert response['data']['username'] == update_body['data']['username'], "Username does not match"
    cleanup(object_id)


def test_update_an_object_negative():
    created_object = new_object()
    object_id = created_object['id']
    update_body_missing_data = {
        "name": "KotUpdated3"
    }
    headers = {'Content-Type': 'application/json'}
    response_missing_data = requests.put(f'http://167.172.172.115:52353/object/{object_id}',
                                         json=update_body_missing_data, headers=headers)
    assert response_missing_data.status_code == 400
    update_body_missing_name = {
        "data": {
            "birthdate": "2026-01-01",
            "color": "GreyUpdated3",
            "name": "KotUpdated3",
            "sex": "MUpdated3",
            "username": "KotSuslikUpdated3"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response_missing_name = requests.put(f'http://167.172.172.115:52353/object/{object_id}',
                                         json=update_body_missing_name, headers=headers)
    assert response_missing_name.status_code == 400
    update_body_invalid_name = {
        "data": {
            "birthdate": "2026-01-01",
            "color": "GreyUpdated3",
            "name": "KotUpdated3",
            "sex": "MUpdated3",
            "username": "KotSuslikUpdated3"
        },
        "name": []
    }
    headers = {'Content-Type': 'application/json'}
    response_invalid_name = requests.put(f'http://167.172.172.115:52353/object/{object_id}',
                                         json=update_body_invalid_name, headers=headers)
    assert response_invalid_name.status_code == 400
    update_body_invalid_data = {
        "data": 1,
        "name": "name"
    }
    headers = {'Content-Type': 'application/json'}
    response_invalid_data = requests.put(f'http://167.172.172.115:52353/object/{object_id}',
                                         json=update_body_invalid_data, headers=headers)
    assert response_invalid_data.status_code == 400
    cleanup(object_id)


def test_patch_an_object_positive():
    created_object = new_object()
    object_id = created_object['id']
    update_partial_body_data = {
        "data": {
            "birthdate": "2027-01-01",
            "color": "WhitePatched",
            "name": "KotPatched",
            "sex": "MPatched",
            "username": "KotBelyPatched"
        }
    }
    headers = {'Content-Type': 'application/json'}
    requests.patch(f'http://167.172.172.115:52353/object/{object_id}',
                   json=update_partial_body_data, headers=headers).json()
    response = requests.get(f'http://167.172.172.115:52353/object/{object_id}').json()
    assert str(response['id']) == str(object_id), "id does not match"
    assert response['data']['color'] == update_partial_body_data['data']['color'], "Color does not match"
    assert response['data']['birthdate'] == update_partial_body_data['data']['birthdate'], "Birthdate does not match"
    assert response['data']['name'] == update_partial_body_data['data']['name'], "Name in data does not match"
    assert response['data']['sex'] == update_partial_body_data['data']['sex'], "Sex does not match"
    assert response['data']['username'] == update_partial_body_data['data']['username'], "Username does not match"
    update_partial_body_name = {
        "name": "KotBelyPatchedPartially"
    }
    headers = {'Content-Type': 'application/json'}
    requests.patch(f'http://167.172.172.115:52353/object/{object_id}',
                   json=update_partial_body_name, headers=headers).json()
    response = requests.get(f'http://167.172.172.115:52353/object/{object_id}').json()
    assert str(response['id']) == str(object_id), "id does not match"
    assert response['name'] == update_partial_body_name['name'], "Name does not match"
    cleanup(object_id)


def test_patch_an_object_negative():
    created_object = new_object()
    object_id = created_object['id']
    patch_body_no_fields = {
    }
    headers = {'Content-Type': 'application/json'}
    response_no_fields = requests.patch(f'http://167.172.172.115:52353/object/{object_id}',
                                        json=patch_body_no_fields, headers=headers)
    assert response_no_fields.status_code == 400
    patch_body_invalid_name = {
        "name": {}
    }
    headers = {'Content-Type': 'application/json'}
    response_patch_invalid_name = requests.patch(f'http://167.172.172.115:52353/object/{object_id}',
                                                 json=patch_body_invalid_name, headers=headers)
    assert response_patch_invalid_name.status_code == 400
    patch_body_invalid_data = {
        "data": 1
    }
    headers = {'Content-Type': 'application/json'}
    response_patch_invalid_data = requests.patch(f'http://167.172.172.115:52353/object/{object_id}',
                                                 json=patch_body_invalid_data, headers=headers)
    assert response_patch_invalid_data.status_code == 400
    cleanup(object_id)


def test_delete_one_object_positive():
    created_object = new_object()
    object_id = created_object['id']
    response = requests.delete(f'http://167.172.172.115:52353/object/{object_id}')
    assert response.status_code == 200


def test_delete_nonexistent_object():
    test_id = '9999'
    delete_response = requests.delete(f'http://167.172.172.115:52353/object/{test_id}')
    assert delete_response.status_code == 404
