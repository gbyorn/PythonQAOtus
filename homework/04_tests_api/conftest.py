import pytest


@pytest.fixture(params=[{"url": "https://api.openbrewerydb.org/breweries/",
                         "city": "san_diego",
                         "state": "new_york",
                         "type": "bar",
                         "id": "/5494",
                         "query": "Brewhouse"}])
def fixture_brewery_params(request):
    return request.param


@pytest.fixture(params=[{"url": "https://jsonplaceholder.typicode.com/posts",
                         "uid": 1,
                         "pid": "/1",
                         "data": {
                            "userId": 4000,
                            "title": "Test Title",
                            "body": "Test messages for test."}}])
def fixture_placeholder_params(request):
    return request.param


@pytest.fixture(params=[{"url": "https://dog.ceo/api",
                         "all": "/breeds/list/all",
                         "hound": {"base": "/breed/hound/",
                                   "list": "list",
                                   "random": "/images/random"},
                         "image": {"all": "/breed/hound/images",
                                   "random": "/breeds/image/random/",
                                   "number": "5"}}])
def fixture_dog_api_params(request):
    return request.param


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        help="This is request url"
    )

    parser.addoption(
        "--code",
        default=200,
        help="This is status code of request"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def code(request):
    return request.config.getoption("--code")
