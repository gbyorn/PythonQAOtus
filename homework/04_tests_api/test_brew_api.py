import requests


class TestBrewery:
    def test_brewery_one(self, fixture_brewery_params):
        response = requests.get(fixture_brewery_params["url"],
                                params={"by_city": fixture_brewery_params["city"]})
        assert response.status_code == 200

    def test_brewery_two(self, fixture_brewery_params):
        response = requests.get(fixture_brewery_params["url"],
                                params={"by_state": fixture_brewery_params["state"]})
        assert response.status_code == 200

    def test_brewery_three(self, fixture_brewery_params):
        response = requests.get(fixture_brewery_params["url"],
                                params={"by_type": fixture_brewery_params["type"]})
        assert response.status_code == 200

    def test_brewery_four(self, fixture_brewery_params):
        response = requests.get(fixture_brewery_params["url"],
                                params={"query": fixture_brewery_params["query"]})
        assert response.status_code == 200

    def test_brewery_five(self, fixture_brewery_params):
        response = requests.get(fixture_brewery_params["url"] +
                                fixture_brewery_params["id"])
        assert response.status_code == 200
