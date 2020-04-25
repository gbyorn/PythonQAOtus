import pytest


@pytest.fixture(params=[1, 2, 3, 4, 5])
def fixture_circle_params(request):
    return request.param


@pytest.fixture(params=[[1, 2, 3], [1, 2, 4], [1, 1, 1], [2, 2, 2], [3, 3, 3]])
def fixture_triangle_params(request):
    return request.param


@pytest.fixture(params=[[1, 2], [4, 6], [5, 3], [2, 2], [4, 1]])
def fixture_rectangle_params(request):
    return request.param


@pytest.fixture(params=[1, 2, 3, 4, 5])
def fixture_square_params(request):
    return request.param
