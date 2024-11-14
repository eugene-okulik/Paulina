import requests
import pytest


@pytest.fixture()
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
    object_data = response.json()
    yield object_data
    requests.delete(f"http://167.172.172.115:52353/object/{object_data['id']}")


@pytest.fixture()
def before_after():
    print('Before test')
    yield
    print('After test')


@pytest.fixture(scope='session')
def test_messages():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.mark.critical
def test_one_object(test_messages, before_after, new_object):
    response = requests.get(f"http://167.172.172.115:52353/object/{new_object['id']}").json()
    print(response)
    assert response['id'] == new_object['id'], "id does not match"
    assert response['name'] == new_object['name'], "Name does not match"
    assert response['data']['color'] == new_object['data']['color'], "Color does not match"
    assert response['data']['birthdate'] == new_object['data']['birthdate'], "Birthdate does not match"
    assert response['data']['name'] == new_object['data']['name'], "Name in data does not match"
    assert response['data']['sex'] == new_object['data']['sex'], "sex does not match"
    assert response['data']['username'] == new_object['data']['username'], "Username does not match"


@pytest.mark.parametrize('positive_bodies', [
    {"name": "Kot Bely", "data": {"color": "White", "birthdate": "2023-01-01", "name": "Kot", "sex": "M",
                                  "username": "KotSuslik"}},
    {"name": "Kot Cherny", "data": {"color": "Black", "birthdate": "2023-01-02", "name": "Kot", "sex": "F",
                                    "username": "KotNoch"}},
    {"name": "Kot Ryjy", "data": {"color": "Red", "birthdate": "2023-01-03", "name": "Kot", "sex": "M",
                                  "username": "KotOgon"}}
])
@pytest.mark.medium
def test_post_an_object_positive(test_messages, before_after, positive_bodies):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=positive_bodies,
        headers=headers
    )
    print(response)
    assert response.status_code == 200, 'Status code is incorrect for data'
    created_object = response.json()
    requests.delete(f"http://167.172.172.115:52353/object/{created_object['id']}")


@pytest.mark.parametrize('negative_bodies', [
    {"name": "Kot Sery"},
    {
        "data": {
            "color": "Grey",
            "birthdate": "2023-01-01",
            "name": "Kot",
            "sex": "M",
            "username": "KotSuslik"
        }
    }, {
        "data": {
            "color": "Grey",
            "birthdate": "2023-01-01",
            "name": "Kot",
            "sex": "M",
            "username": "KotSuslik"
        },
        "name": 1234
    }, {
        "data": [{
            "color": "Grey",
            "birthdate": "2023-01-01",
            "name": "Kot",
            "sex": "M",
            "username": "KotSuslik"
        }],
        "name": "Lopata"
    }])
def test_post_an_object_negative(test_messages, before_after, negative_bodies):
    headers = {'Content-Type': 'application/json'}
    response_missing_data = requests.post(
        'http://167.172.172.115:52353/object',
        json=negative_bodies,
        headers=headers
    )
    print(response_missing_data)
    assert response_missing_data.status_code == 400, 'Status code is incorrect for missing data'


def test_update_an_object_positive(test_messages, before_after, new_object):
    object_id = new_object['id']
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


@pytest.mark.parametrize('negative_update_bodies', [{
        "data": {
            "birthdate": "2026-01-01",
            "color": "GreyUpdated3",
            "name": "KotUpdated3",
            "sex": "MUpdated3",
            "username": "KotSuslikUpdated3"
        }
    }, {
        "data": {
            "birthdate": "2026-01-01",
            "color": "GreyUpdated3",
            "name": "KotUpdated3",
            "sex": "MUpdated3",
            "username": "KotSuslikUpdated3"
        },
        "name": []
    }, {
        "data": 1,
        "name": "name"
    }])
def test_update_an_object_negative(test_messages, before_after, new_object, negative_update_bodies):
    object_id = new_object['id']
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'http://167.172.172.115:52353/object/{object_id}',
                            json=negative_update_bodies, headers=headers)
    assert response.status_code == 400


def test_patch_an_object_positive(test_messages, before_after, new_object):
    object_id = new_object['id']
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


@pytest.mark.parametrize('negative_patch_bodies', [{
        "name": {}
    }, {
        "data": 1
    }])
def test_patch_an_object_negative(test_messages, before_after, new_object, negative_patch_bodies):
    object_id = new_object['id']
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'http://167.172.172.115:52353/object/{object_id}',
                              json=negative_patch_bodies, headers=headers)
    assert response.status_code == 400


def test_delete_one_object_positive(test_messages, before_after, new_object):
    object_id = new_object['id']
    response = requests.delete(f'http://167.172.172.115:52353/object/{object_id}')
    assert response.status_code == 200


def test_delete_nonexistent_object(test_messages, before_after):
    test_id = '99999'
    delete_response = requests.delete(f'http://167.172.172.115:52353/object/{test_id}')
    assert delete_response.status_code == 404
