from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK, HTTP_403_FORBIDDEN, HTTP_201_CREATED
from rest_framework.test import APIClient
from rest_framework_simplejwt.models import TokenUser

from clients.models import Client
from portfolios.models import Portfolio


class TestClientView(TestCase):

    def setUp(self) -> None:
        self.api_client = APIClient()
        Client.objects.create(name="Pruebita", last_user="admin", id_last_user=1)

    def test_get_no_token_provided(self):
        url = reverse('client-list')
        result = self.api_client.get(url)
        self.assertEqual(HTTP_401_UNAUTHORIZED, result.status_code)

    def test_get_invalid_token(self):
        url = reverse('client-list')
        token = 'sarlanga'
        result = self.api_client.get(url,{}, HTTP_AUTHORIZATION='Bearer {}'.format(str(token)))
        self.assertEqual(HTTP_401_UNAUTHORIZED, result.status_code)

    def test_get_success_response(self):
        url = reverse('client-list')
        user = TokenUser({'roles':['Supervisor']})
        self.api_client.force_authenticate(user=user)
        result = self.api_client.get(url,{})
        self.assertEqual(HTTP_200_OK, result.status_code)

    def test_get_forbidden(self):
        url = reverse('client-list')
        user = TokenUser({'roles': ['Agente']})
        self.api_client.force_authenticate(user=user)
        result = self.api_client.get(url, {})
        self.assertEqual(HTTP_403_FORBIDDEN, result.status_code)

    def test_post_agente_forbidden(self):
        url = reverse('client-list')
        user = TokenUser({'roles': ['Agente']})
        self.api_client.force_authenticate(user=user)
        result = self.api_client.post(url, {'name': "Poronga"})
        self.assertEqual(HTTP_403_FORBIDDEN, result.status_code)

    def test_post_supervisor_forbidden(self):
        url = reverse('client-list')
        user = TokenUser({'roles': ['Supervisor']})
        self.api_client.force_authenticate(user=user)
        result = self.api_client.post(url, {'name': "Poronga"})
        self.assertEqual(HTTP_403_FORBIDDEN, result.status_code)

    def test_post_success(self):
        url = reverse('client-list')
        user = TokenUser({'roles': ['Backoffice']})
        self.api_client.force_authenticate(user=user)
        result = self.api_client.post(url, {'name': "Poronga"})
        self.assertEqual(HTTP_201_CREATED, result.status_code)
        result = self.api_client.get(url)
        self.assertEqual(HTTP_200_OK, result.status_code)


class TestPortfolioView(TestCase):

    def setUp(self) -> None:
        self.api_client = APIClient()
        Client.objects.create(name="Pruebita carteras", last_user="admin", id_last_user=1)
        Portfolio.objects.create(name="Carteruni", last_user="admin", id_last_user=1, client=Client.objects.first())

    def test_get_no_token_provided(self):
        url = reverse('portfolio-list')
        result = self.api_client.get(url)
        self.assertEqual(HTTP_401_UNAUTHORIZED, result.status_code)

    def test_get_invalid_token(self):
        url = reverse('portfolio-list')
        token = 'sarlanga'
        result = self.api_client.get(url,{}, HTTP_AUTHORIZATION='Bearer {}'.format(str(token)))
        self.assertEqual(HTTP_401_UNAUTHORIZED, result.status_code)

    def test_get_success_response(self):
        url = reverse('portfolio-list')
        user = TokenUser({'roles':['Supervisor']})
        self.api_client.force_authenticate(user=user)
        result = self.api_client.get(url,{})
        self.assertEqual(HTTP_200_OK, result.status_code)

    def test_get_forbidden(self):
        url = reverse('portfolio-list')
        user = TokenUser({'roles': ['Agente']})
        self.api_client.force_authenticate(user=user)
        result = self.api_client.get(url, {})
        self.assertEqual(HTTP_403_FORBIDDEN, result.status_code)

    def test_post_agente_forbidden(self):
        url = reverse('portfolio-list')
        user = TokenUser({'roles': ['Agente']})
        self.api_client.force_authenticate(user=user)
        result = self.api_client.post(url, {'name': "Poronga"})
        self.assertEqual(HTTP_403_FORBIDDEN, result.status_code)

    def test_post_success(self):
        url = reverse('portfolio-list')
        user = TokenUser({'roles': ['Backoffice']})
        self.api_client.force_authenticate(user=user)
        result = self.api_client.post(url, {'name': "Poronga"})
        self.assertEqual(HTTP_201_CREATED, result.status_code)
        result = self.api_client.get(url)
        self.assertEqual(HTTP_200_OK, result.status_code)
