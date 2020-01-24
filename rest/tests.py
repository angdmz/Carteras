from collections import namedtuple

from django.test import TestCase, RequestFactory

# Create your tests here.
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.models import TokenUser

from clients.models import Client
from rest.security import IsSupervisorOrHigher
from rest.views import ClientViewSet


class TestPermission(TestCase):
    def test_is_supervisor(self):
        permission = IsSupervisorOrHigher()
        request = namedtuple('Request', 'user')
        user = TokenUser({'roles':['Supervisor']})
        request.user = user
        has_permission = permission.has_permission(request, user)
        self.assertTrue(has_permission)

    def test_is_agente(self):
        permission = IsSupervisorOrHigher()
        request = namedtuple('Request', 'user')
        user = TokenUser({'roles':['Agente']})
        request.user = user
        has_permission = permission.has_permission(request, user)
        self.assertFalse(has_permission)

    def test_is_agente_and_backoffice(self):
        permission = IsSupervisorOrHigher()
        request = namedtuple('Request', 'user')
        user = TokenUser({'roles':['Agente', 'Backoffice']})
        request.user = user
        has_permission = permission.has_permission(request, user)
        self.assertTrue(has_permission)

    def test_no_role_assigned(self):
        permission = IsSupervisorOrHigher()
        request = namedtuple('Request', 'user')
        user = TokenUser({})
        request.user = user
        has_permission = permission.has_permission(request, user)
        self.assertFalse(has_permission)


class TestClientView(TestCase):

    def setUp(self) -> None:
        self.request_factory = APIRequestFactory()
        Client.objects.create(name="Pruebita", last_user="admin", id_last_user=1)

    def test_no_token_provided(self):
        request = self.request_factory.get('/v1/clients/')
        view = ClientViewSet()
        response = view.dispatch(request)
        self.assertEqual(401, response.status_code)
