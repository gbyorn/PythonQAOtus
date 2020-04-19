import requests


class TestPlaceholder:
    def test_placeholder_one(self, fixture_placeholder_params):
        response = requests.get(fixture_placeholder_params["url"])
        assert response.status_code == 200

    def test_placeholder_two(self, fixture_placeholder_params):
        response = requests.get(fixture_placeholder_params["url"],
                                params={'userId': fixture_placeholder_params["uid"]})
        assert response.text

    def test_placeholder_three(self, fixture_placeholder_params):
        response = requests.post(fixture_placeholder_params["url"],
                                 fixture_placeholder_params["data"])
        assert response.status_code == 201

    def test_placeholder_four(self, fixture_placeholder_params):
        response = requests.patch(fixture_placeholder_params["url"] + fixture_placeholder_params["pid"],
                                  fixture_placeholder_params["data"])
        assert response.status_code == 200

    def test_placeholder_five(self, fixture_placeholder_params):
        response = requests.delete(fixture_placeholder_params["url"] + fixture_placeholder_params["pid"])
        assert response.status_code == 200
