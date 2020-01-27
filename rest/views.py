from django.shortcuts import render

# Create your views here.
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from clients.models import Client
from clients.serializers import ClientSerializer
from portfolios.models import Portfolio
from portfolios.serializers import PortfolioSerializer
from rest.security import IsSupervisorOrHigher


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    authentication_classes = (JWTTokenUserAuthentication ,)
    permission_classes = (IsSupervisorOrHigher, )
    queryset = Client.objects.all()
    pagination_class = LimitOffsetPagination


class PortfoliosViewSet(ModelViewSet):
    serializer_class = PortfolioSerializer
    authentication_classes = (JWTTokenUserAuthentication ,)
    permission_classes = (IsSupervisorOrHigher, )
    queryset = Portfolio.objects.all()
    pagination_class = LimitOffsetPagination
