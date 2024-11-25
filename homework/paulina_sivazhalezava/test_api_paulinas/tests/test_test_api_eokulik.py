import pytest
import allure

TEST_DATA_POSITIVE = [
    {"name": "Kot Bely", "data": {"color": "White", "birthdate": "2023-01-01", "name": "Kot", "sex": "M",
                                  "username": "KotSuslik"}},
    {"name": "Kot Cherny", "data": {"color": "Black", "birthdate": "2023-01-02", "name": "Kot", "sex": "F",
                                    "username": "KotNoch"}},
    {"name": "Kot Ryjy", "data": {"color": "Red", "birthdate": "2023-01-03", "name": "Kot", "sex": "M",
                                  "username": "KotOgon"}}
]

TEST_DATA_NEGATIVE = [
    {"name": "Kot Sery"},
    {"data": {"color": "Grey", "birthdate": "2023-01-02", "name": "Kot", "sex": "F",
              "username": "KotSusLik"}},
    {"name": 1234, "data": {"color": "Red", "birthdate": "2023-01-03", "name": "Kot", "sex": "M",
                            "username": "KotHtl"}}
]


@allure.feature('Manipulate object')
@allure.story('Object create')
@allure.title('Test posting an object with valid body data')
@allure.link(url='https://masterpiecer-images.s3.yandex.net/010b92c1914b11ee9e3192669a1675b3:upscaled',
             name='Cats description specification')
@pytest.mark.parametrize('data', TEST_DATA_POSITIVE)
@pytest.mark.medium
def test_post_an_object_positive(create_object_endpoint, data, cleanup_object):
    create_object_endpoint.create_new_object(payload=data)
    create_object_endpoint.check_that_status_code_is_200()
    cleanup_object.append(create_object_endpoint.object_id)


@allure.feature('Manipulate object')
@allure.story('Object create')
@allure.title('Test posting an object with invalid body data')
@pytest.mark.parametrize('data', TEST_DATA_NEGATIVE)
def test_post_an_object_negative(create_object_endpoint, data):
    create_object_endpoint.create_new_object(payload=data)
    create_object_endpoint.check_that_status_code_is_400()


@allure.feature('Manipulate object')
@allure.story('Object deletion')
@allure.title('Test deleting an existing object')
def test_delete_one_object_positive(create_test_object, delete_object_endpoint):
    object_id = create_test_object
    delete_object_endpoint.delete_object(object_id=object_id)
    delete_object_endpoint.check_that_status_code_is_200()


@allure.story('Object deletion')
@allure.feature('Manipulate object')
@allure.title('Test attempt to delete a non-existent object')
def test_delete_nonexistent_object(delete_object_endpoint):
    delete_object_endpoint.delete_object(object_id=999999)
    delete_object_endpoint.check_that_status_code_is_404()


@allure.feature('Retrieve object')
@allure.story('Object get')
@allure.title('Test fetching a single object')
@pytest.mark.critical
def test_get_one_object_positive(create_test_object, get_object_endpoint):
    object_id = create_test_object
    expected_data = {
        "name": "Kot Bonifacy",
        "data": {
            "color": "Red",
            "birthdate": "2022-01-01",
            "name": "Bonifacy",
            "sex": "M",
            "username": "KotBonifacyStary"
        }
    }
    get_object_endpoint.get_an_object(object_id=object_id)
    get_object_endpoint.check_that_status_code_is_200()
    get_object_endpoint.check_that_id_is_correct(expected_id=object_id)
    get_object_endpoint.check_that_name_is_correct(expected_name=expected_data["name"])
    get_object_endpoint.check_that_color_is_correct(expected_color=expected_data["data"]["color"])
    get_object_endpoint.check_that_birthdate_is_correct(expected_birthdate=expected_data["data"]["birthdate"])
    get_object_endpoint.check_that_name_in_data_is_correct(expected_name_in_data=expected_data["data"]["name"])
    get_object_endpoint.check_that_sex_is_correct(expected_sex=expected_data["data"]["sex"])
    get_object_endpoint.check_that_username_is_correct(expected_username=expected_data["data"]["username"])


@allure.feature('Manipulate object')
@allure.story('Object update')
@allure.title('Test updating an object with valid data')
def test_update_one_object_positive(create_test_object, update_object_endpoint, get_object_endpoint):
    object_id = create_test_object
    new_payload = {
        "data": {
            "color": "RedUpdated",
            "birthdate": "2020-01-02",
            "name": "LeopoldUpdated",
            "sex": "M",
            "username": "KotLeopoldUpdated"
        },
        "name": "Kot Leopold Updated"
    }
    update_object_endpoint.update_new_object(object_id=object_id, payload=new_payload)
    get_object_endpoint.get_an_object(object_id=update_object_endpoint.object_id)
    get_object_endpoint.check_that_status_code_is_200()
    get_object_endpoint.check_that_id_is_correct(expected_id=update_object_endpoint.object_id)
    get_object_endpoint.check_that_name_is_correct(expected_name=new_payload["name"])
    get_object_endpoint.check_that_color_is_correct(expected_color=new_payload["data"]["color"])
    get_object_endpoint.check_that_birthdate_is_correct(expected_birthdate=new_payload["data"]["birthdate"])
    get_object_endpoint.check_that_name_in_data_is_correct(expected_name_in_data=new_payload["data"]["name"])
    get_object_endpoint.check_that_sex_is_correct(expected_sex=new_payload["data"]["sex"])
    get_object_endpoint.check_that_username_is_correct(expected_username=new_payload["data"]["username"])


TEST_DATA_UPDATE_NEGATIVE = [
    {
        "name": "Kot Polosaty"
    },
    {
        "data": {
            "color": "Grey",
            "birthdate": "2023-01-02",
            "name": "Kot",
            "sex": "F",
            "username": "KotSusLik"
        },
        "name": []
    },
    {
        "name": 1234,
        "data": {
            "color": "Yellow",
            "birthdate": "2023-01-03",
            "name": "Kot",
            "sex": "M",
            "username": "KotYello"
        }
    }
]


@allure.feature('Manipulate object')
@allure.story('Object update')
@allure.title('Test updating an object with invalid data')
@pytest.mark.parametrize('data', TEST_DATA_UPDATE_NEGATIVE)
def test_update_one_object_negative(create_test_object, update_object_endpoint, data):
    object_id = create_test_object
    update_object_endpoint.update_new_object(object_id=object_id, payload=data)
    update_object_endpoint.check_that_status_code_is_400()


@allure.feature('Manipulate object')
@allure.story('Object patch')
@allure.title('Test partial update (patch) of an object with valid data')
def test_patch_one_object_positive(create_test_object, patch_object_endpoint, get_object_endpoint):
    object_id = create_test_object
    new_patch_payload = {
        "data": {
            "birthdate": "2027-01-01",
            "color": "TomPatched",
            "name": "KotPatched",
            "sex": "MPatched",
            "username": "KotTomPatched"
        }
    }
    patch_object_endpoint.patch_new_object(object_id=object_id, payload=new_patch_payload)
    get_object_endpoint.get_an_object(object_id=patch_object_endpoint.object_id)
    get_object_endpoint.check_that_status_code_is_200()
    get_object_endpoint.check_that_id_is_correct(expected_id=patch_object_endpoint.object_id)
    get_object_endpoint.check_that_color_is_correct(expected_color=new_patch_payload["data"]["color"])
    get_object_endpoint.check_that_birthdate_is_correct(expected_birthdate=new_patch_payload["data"]["birthdate"])
    get_object_endpoint.check_that_name_in_data_is_correct(expected_name_in_data=new_patch_payload["data"]["name"])
    get_object_endpoint.check_that_sex_is_correct(expected_sex=new_patch_payload["data"]["sex"])
    get_object_endpoint.check_that_username_is_correct(expected_username=new_patch_payload["data"]["username"])


TEST_DATA_PATCH_NEGATIVE = [
    {
        "name": {}
    },
    {
        "data": 1
    }
]


@allure.feature('Manipulate object')
@allure.story('Object patch')
@allure.title('Test partial update (patch) of an object with invalid data')
@pytest.mark.parametrize('data', TEST_DATA_PATCH_NEGATIVE)
def test_patch_one_object_negative(create_test_object, patch_object_endpoint, data):
    object_id = create_test_object
    patch_object_endpoint.patch_new_object(object_id=object_id, payload=data)
    patch_object_endpoint.check_that_status_code_is_400()
