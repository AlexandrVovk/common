from http import HTTPStatus
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.conf import settings
import requests

POCKEMON_URL = settings.POCKEMON_URL
response_api_pokemon = requests.get(f'{POCKEMON_URL}/type/3')
response_api_pokemon_bad_structure = requests.get(f'{POCKEMON_URL}')


class StatusViewTests(TestCase):
    client = Client()

    def test_index_func_view(self):
        response = self.client.get(reverse('index_func'))
        assert response.status_code == HTTPStatus.OK

    def test_healthcheck_view(self):
        response = self.client.get(reverse('health_check'))
        assert response.status_code == HTTPStatus.OK

    def test_list_func_view(self):
        response = self.client.get(reverse('list_func'))
        assert response.status_code == HTTPStatus.OK

    def test_pokemon_api_response_dict(self):
        self.assertIsInstance(response_api_pokemon.json(), dict)

    def test_pokemon_api_response_structure(self):
        result = ['name', 'url']
        for item in response_api_pokemon.json()['pokemon']:
            actual_result = list(item['pokemon'].keys())
            self.assertEqual(result, actual_result)

    def test_pokemon_api_response_bad_structure(self):
        try:
            response_api_pokemon_bad_structure.json()['pokemon']['pokemon']
            assert False
        except:
            assert True
