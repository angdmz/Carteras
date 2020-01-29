from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from portfolios.models import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):

    def get_client_name(self, obj):
        return obj.client.name if obj.client is not None else None

    def get_client_id(self, obj):
        return obj.client_id

    client_name = SerializerMethodField()

    class Meta:
        model = Portfolio
        fields = ['id', 'name', 'last_user', 'id_last_user', 'add_date', 'last_modification', 'tasa_honorarios', 'client_name', 'client_id']