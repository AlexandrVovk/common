from http import HTTPStatus

from django.test import TestCase
from django.test import Client

from django.urls import reverse


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