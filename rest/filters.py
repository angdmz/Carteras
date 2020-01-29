import django_filters
from django.db.models import Q

from portfolios.models import Portfolio


class ListFilter(django_filters.Filter):
    def filter(self, qs, value):
        if not value:
            return qs

        self.lookup_expr = 'in'
        values = value.split(',')

        if 'null' in values:
            values.remove('null')
            qs = qs.filter(Q(**{'%s__%s' % (self.name, 'isnull'): True}) | Q(**{'%s__%s' % (self.name, 'in'): values}))
            return qs
        else:
            return super(ListFilter, self).filter(qs, values)

class PortfolioFilter(django_filters.FilterSet):
    client_id = ListFilter(field_name='client_id')

    class Meta:
        model = Portfolio
        fields = ['client_id', 'name']
