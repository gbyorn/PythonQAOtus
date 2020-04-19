import requests
import json
import random


class TestDogApi:
    def test_dog_api_one(self, fixture_dog_api_params):
        response = requests.get(fixture_dog_api_params["url"] +
                                fixture_dog_api_params["all"])
        assert response.text

    def test_dog_api_two(self, fixture_dog_api_params):
        response = requests.get(fixture_dog_api_params["url"] +
                                fixture_dog_api_params["image"]["all"])
        assert response.status_code == 200

    def test_dog_api_three(self, fixture_dog_api_params):
        response = requests.get(fixture_dog_api_params["url"] +
                                fixture_dog_api_params["image"]["random"] +
                                fixture_dog_api_params["image"]["number"])
        assert len(json.loads(response.text)["message"]) == int(fixture_dog_api_params["image"]["number"])

    def test_dog_api_four(self, fixture_dog_api_params):
        response = requests.get(fixture_dog_api_params["url"] +
                                fixture_dog_api_params["hound"]["base"] +
                                fixture_dog_api_params["hound"]["list"])
        assert response.status_code == 200

    def test_dog_api_five(self, fixture_dog_api_params):
        response = requests.get(fixture_dog_api_params["url"] +
                                fixture_dog_api_params["hound"]["base"] +
                                fixture_dog_api_params["hound"]["list"])
        hounds = json.loads(response.text)["message"]
        response = requests.get(fixture_dog_api_params["url"] +
                                fixture_dog_api_params["hound"]["base"] +
                                random.choice(hounds) +
                                fixture_dog_api_params["hound"]["random"])
        assert response.status_code == 200
