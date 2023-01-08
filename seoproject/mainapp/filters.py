"""
'exact' - полное совпадения названия, например 'НИАРМЕДИК'
'iexact' - работает также как 'exact'
'contains' - любое совпадение, но с учетом регистра букв
'icontains' - работает также как 'contains'
'regex' - Наименование клиники соответствует регулярному выражению
'iregex' - любые буквы или сочетания без учета регистра
"""
import django_filters
from .models import Company

# refer to 'django_filters.conf.DEFAULTS'


class CompanyFilter(django_filters.FilterSet):

    class Meta:
        model = Company

        fields = {
                    'name': ['iregex'],
                    'rating': ['gte'],
                    'time_create': ['iregex'],
                  }
