from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from clients.models import Client
from clients.serializers import ClientSerializer


class IsSupervisorOrHigher(BasePermission):

    def has_permission(self, request, view):
        return any(x in request.user.token.get('roles', []) for x in ['Administrador', 'Jefe de operaciones', 'Supervisor', 'Backoffice', 'Desarrollador', 'Operaciones'])
