from rest_framework import serializers

from portfolios.models import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id', 'name', 'last_user', 'id_last_user', 'add_date', 'last_modification', 'tasa_honorarios', 'client']