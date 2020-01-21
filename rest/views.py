from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from clients.models import Client


class ClientViewSet(ModelViewSet):
    permission_classes = (JWTAuthentication, IsAuthenticated, )
    queryset = Client.objects.all()
