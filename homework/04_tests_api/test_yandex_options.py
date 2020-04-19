import requests


def test_ya_api(url, code):
    assert requests.get(url).status_code == int(code)
