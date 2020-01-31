from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from clients.models import Client
from portfolios.models import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):

    client_manager = Client.objects
    portfolio_manager = Portfolio.objects

    def get_client_name(self, obj):
        return obj.client.name if obj.client is not None else None

    client_name = SerializerMethodField()

    def validate(self, attrs):
        if not 'client_id' in attrs:
            raise serializers.ValidationError("No client id set")

        if not self.client_manager.filter(pk=attrs['client_id']).exists():
            raise serializers.ValidationError("No client with {}".format(str(attrs['client_id'])))

        return attrs

    def create(self, validated_data):
        client = self.client_manager.get(pk=validated_data['client_id'])
        validated_data['client'] = client
        portfolio = self.portfolio_manager.create(**validated_data)
        return portfolio

    class Meta:
        model = Portfolio
        fields = ['id', 'name', 'last_user', 'id_last_user', 'add_date', 'last_modification', 'tasa_honorarios', 'client_name', 'client_id']