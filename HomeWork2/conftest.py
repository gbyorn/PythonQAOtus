import pytest


@pytest.fixture(params=[[11, 12, 13, 14, 15]])
def fixture_list_params(request):
    return request.param


@pytest.fixture(params=[{21, 22, 23, 24, 25}])
def fixture_set_params(request):
    return request.param


@pytest.fixture(params=[{'31': 1, '32': 2, '33': 3, '34': 4, '35': 5}])
def fixture_dict_params(request):
    return request.param


@pytest.fixture(params=["12345"])
def fixture_string_params(request):
    return request.param
