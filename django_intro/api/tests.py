from http import HTTPStatus

from django.test import TestCase
from django.test import Client

from django.urls import reverse
# from api.views import POCKEMON_URL
import requests

POCKEMON_URL = 'https://pokeapi.co/api/v2/'
response_api_pokemon = requests.get(f'{POCKEMON_URL}/type/3')
response_api_pokemon_bad = requests.get(f'{POCKEMON_URL}/type/33333')

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
        result = type(dict())
        actual_result = type(response_api_pokemon.json())
        self.assertEqual(result, actual_result)

    def test_pokemon_api_response_structure(self):
        result = ['name', 'url']
        for item in response_api_pokemon.json()['pokemon']:
            actual_result = list(item['pokemon'].keys())
            self.assertEqual(result, actual_result)
