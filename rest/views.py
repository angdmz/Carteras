# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from clients.models import Client
from clients.serializers import ClientSerializer
from portfolios.models import Portfolio
from portfolios.serializers import PortfolioSerializer
from rest.filters import PortfolioFilter
from rest.security import ClientServicePermission


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    authentication_classes = (JWTTokenUserAuthentication ,)
    permission_classes = (ClientServicePermission,)
    queryset = Client.objects.prefetch_related('portfolios').all()
    pagination_class = LimitOffsetPagination


class PortfoliosViewSet(ModelViewSet):
    serializer_class = PortfolioSerializer
    authentication_classes = (JWTTokenUserAuthentication ,)
    permission_classes = (ClientServicePermission,)
    queryset = Portfolio.objects.select_related('client').all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = PortfolioFilter
    pagination_class = LimitOffsetPagination
