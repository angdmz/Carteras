from collections import namedtuple

from django.contrib.auth.models import AnonymousUser
from django.test import TestCase
from rest_framework_simplejwt.models import TokenUser

from rest.security import ClientServicePermission


class TestClientPermission(TestCase):

    def create_mocks(self, user, action):
        request = namedtuple('Request', 'user view',)
        view = namedtuple('View', 'action',)
        view.action = action
        request.user = user
        return request, view

    def test_is_supervisor(self):
        permission = ClientServicePermission()
        user = TokenUser({'roles':['Supervisor']})
        request, view = self.create_mocks(user, 'list')
        has_permission = permission.has_permission(request, view)
        self.assertTrue(has_permission)
        request, view = self.create_mocks(user, 'create')
        has_permission = permission.has_permission(request, view)
        self.assertFalse(has_permission)

    def test_is_agente(self):
        permission = ClientServicePermission()
        user = TokenUser({'roles':['Agente']})
        request, view = self.create_mocks(user, 'list')
        has_permission = permission.has_permission(request, view)
        self.assertFalse(has_permission)
        request, view = self.create_mocks(user, 'create')
        has_permission = permission.has_permission(request, view)
        self.assertFalse(has_permission)


    def test_is_agente_and_backoffice(self):
        permission = ClientServicePermission()
        user = TokenUser({'roles':['Agente', 'Backoffice']})
        request, view = self.create_mocks(user, 'list')
        has_permission = permission.has_permission(request, view)
        self.assertTrue(has_permission)
        request, view = self.create_mocks(user, 'create')
        has_permission = permission.has_permission(request, view)
        self.assertTrue(has_permission)

    def test_no_role_assigned(self):
        permission = ClientServicePermission()
        user = TokenUser({})
        request, view = self.create_mocks(user, 'list')
        has_permission = permission.has_permission(request, view)
        self.assertFalse(has_permission)
        request, view = self.create_mocks(user, 'create')
        has_permission = permission.has_permission(request, view)
        self.assertFalse(has_permission)

    def test_unauthenticated(self):
        permission = ClientServicePermission()
        user = AnonymousUser()
        request, view = self.create_mocks(user, 'list')
        has_permission = permission.has_permission(request, view)
        self.assertFalse(has_permission)
        request, view = self.create_mocks(user, 'create')
        has_permission = permission.has_permission(request, view)
        self.assertFalse(has_permission)