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
def test_delete_one_object_positive(create_object_endpoint, delete_object_endpoint):
    create_object_endpoint.create_new_object(payload={

        "data": {
            "color": "Red",
            "birthdate": "2022-01-01",
            "name": "Bonifacy",
            "sex": "M",
            "username": "KotBonifacyStary"
        },
        "name": "Kot Bonifacy"
    })
    delete_object_endpoint.delete_object(object_id=create_object_endpoint.object_id)
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
def test_get_one_object_positive(create_object_endpoint, get_object_endpoint, cleanup_object):
    create_object_endpoint.create_new_object(payload={

        "data": {
            "color": "Tabby",
            "birthdate": "2022-01-01",
            "name": "Suslik",
            "sex": "M",
            "username": "KotSuslik"
        },
        "name": "Kot Suslik"
    })
    get_object_endpoint.get_an_object(object_id=create_object_endpoint.object_id)
    get_object_endpoint.check_that_status_code_is_200()
    get_object_endpoint.check_that_id_is_correct()
    get_object_endpoint.check_that_name_is_correct()
    get_object_endpoint.check_that_color_is_correct()
    get_object_endpoint.check_that_birthdate_is_correct()
    get_object_endpoint.check_that_name_in_data_is_correct()
    get_object_endpoint.check_that_sex_is_correct()
    get_object_endpoint.check_that_username_is_correct()
    cleanup_object.append(create_object_endpoint.object_id)


@allure.feature('Manipulate object')
@allure.story('Object update')
@allure.title('Test updating an object with valid data')
def test_update_one_object_positive(create_object_endpoint, update_object_endpoint, get_object_endpoint,
                                    cleanup_object):
    create_object_endpoint.create_new_object(payload={

        "data": {
            "color": "Red",
            "birthdate": "2020-01-01",
            "name": "Leopold",
            "sex": "M",
            "username": "KotLeopold"
        },
        "name": "Kot Leopold"
    })
    update_object_endpoint.update_new_object(object_id=create_object_endpoint.object_id, payload={

        "data": {
            "color": "RedUpdated",
            "birthdate": "2020-01-02",
            "name": "LeopoldUpdated",
            "sex": "M",
            "username": "KotLeopoldUpdated"
        },
        "name": "Kot Leopold Updated"
    })
    get_object_endpoint.get_an_object(object_id=update_object_endpoint.object_id)
    get_object_endpoint.check_that_status_code_is_200()
    get_object_endpoint.check_that_id_is_correct()
    get_object_endpoint.check_that_name_is_correct()
    get_object_endpoint.check_that_color_is_correct()
    get_object_endpoint.check_that_birthdate_is_correct()
    get_object_endpoint.check_that_name_in_data_is_correct()
    get_object_endpoint.check_that_sex_is_correct()
    get_object_endpoint.check_that_username_is_correct()
    cleanup_object.append(create_object_endpoint.object_id)


TEST_DATA_UPDATE_NEGATIVE = [
        {"name": "Kot Polosaty"},
        {"data": {"color": "Grey", "birthdate": "2023-01-02", "name": "Kot", "sex": "F",
                  "username": "KotSusLik"}, "name": []},
        {"name": 1234, "data": {"color": "Yellow", "birthdate": "2023-01-03", "name": "Kot", "sex": "M",
                                "username": "KotYello"}}
    ]


@allure.feature('Manipulate object')
@allure.story('Object update')
@allure.title('Test updating an object with invalid data')
@pytest.mark.parametrize('data', TEST_DATA_UPDATE_NEGATIVE)
def test_update_one_object_negative(create_object_endpoint, update_object_endpoint, data, cleanup_object):
    create_object_endpoint.create_new_object(payload={

        "data": {
            "color": "Green",
            "birthdate": "2020-01-01",
            "name": "Tito",
            "sex": "M",
            "username": "KotTito"
        },
        "name": "Kot Tito"
    })
    update_object_endpoint.update_new_object(object_id=create_object_endpoint.object_id, payload=data)
    update_object_endpoint.check_that_status_code_is_400()
    cleanup_object.append(create_object_endpoint.object_id)


@allure.feature('Manipulate object')
@allure.story('Object patch')
@allure.title('Test partial update (patch) of an object with valid data')
def test_patch_one_object_positive(create_object_endpoint, patch_object_endpoint, get_object_endpoint, cleanup_object):
    create_object_endpoint.create_new_object(payload={

        "data": {
            "color": "Brown",
            "birthdate": "2020-01-01",
            "name": "Tom",
            "sex": "M",
            "username": "KotTom"
        },
        "name": "Kot Tom"
    })
    patch_object_endpoint.patch_new_object(object_id=create_object_endpoint.object_id, payload={
            "data": {
                "birthdate": "2027-01-01",
                "color": "TomPatched",
                "name": "KotPatched",
                "sex": "MPatched",
                "username": "KotTomPatched"
            }
        })
    get_object_endpoint.get_an_object(object_id=patch_object_endpoint.object_id)
    get_object_endpoint.check_that_status_code_is_200()
    get_object_endpoint.check_that_id_is_correct()
    get_object_endpoint.check_that_color_is_correct()
    get_object_endpoint.check_that_birthdate_is_correct()
    get_object_endpoint.check_that_name_in_data_is_correct()
    get_object_endpoint.check_that_sex_is_correct()
    get_object_endpoint.check_that_username_is_correct()
    cleanup_object.append(create_object_endpoint.object_id)


TEST_DATA_PATCH_NEGATIVE = [
    {
        "name": {}
    }, {
        "data": 1
    }
    ]


@allure.feature('Manipulate object')
@allure.story('Object patch')
@allure.title('Test partial update (patch) of an object with invalid data')
@pytest.mark.parametrize('data', TEST_DATA_PATCH_NEGATIVE)
def test_patch_one_object_negative(create_object_endpoint, patch_object_endpoint, data, cleanup_object):
    create_object_endpoint.create_new_object(payload={

        "data": {
            "color": "Blue",
            "birthdate": "2019-01-01",
            "name": "Sam",
            "sex": "M",
            "username": "KotSam"
        },
        "name": "Kot Sam"
    })
    patch_object_endpoint.patch_new_object(object_id=create_object_endpoint.object_id, payload=data)
    patch_object_endpoint.check_that_status_code_is_400()
    cleanup_object.append(create_object_endpoint.object_id)
