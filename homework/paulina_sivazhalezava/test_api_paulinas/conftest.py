import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from endpoints.patch_object import PatchObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def get_object_endpoint():
    return GetObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def patch_object_endpoint():
    return PatchObject()


@pytest.fixture()
def cleanup_object(delete_object_endpoint):
    created_object_ids = []

    yield created_object_ids

    for object_id in created_object_ids:
        delete_object_endpoint.delete_object(object_id)
