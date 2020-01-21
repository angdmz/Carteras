from rest_framework import serializers

from clients.models import Client
from portfolios.serializers import PortfolioSerializer


class ClientSerializer(serializers.ModelSerializer):

    portfolios = PortfolioSerializer(many=True)

    class Meta:
        model = Client
        fields = ['id', 'name', 'last_user', 'id_last_user', 'add_date', 'last_modification', 'portfolios']