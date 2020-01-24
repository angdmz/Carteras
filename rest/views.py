from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from clients.models import Client
from clients.serializers import ClientSerializer
from rest.security import IsSupervisorOrHigher


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    authentication_classes = (JWTTokenUserAuthentication ,)
    permission_classes = (IsSupervisorOrHigher, )
    queryset = Client.objects.all()
