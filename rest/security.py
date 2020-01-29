from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from clients.models import Client
from clients.serializers import ClientSerializer

class ClientServicePermission(BasePermission):

    roles_per_action = {
        'create': ['Administrador', 'Jefe de operaciones', 'Backoffice', 'Desarrollador', 'Operaciones'],
        'list': ['Administrador', 'Jefe de operaciones', 'Supervisor', 'Backoffice', 'Desarrollador', 'Operaciones']
    }

    def has_permission(self, request, view):
        return request.user.is_authenticated and any(x in request.user.token.get('roles', []) for x in self.roles_per_action[view.action])

