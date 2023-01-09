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
    name = django_filters.CharFilter(lookup_expr='iregex', label='Клиника')
    rating = django_filters.NumberFilter(lookup_expr='gte', label='Рейтинг')
    # tag = django_filters.CharFilter(lookup_expr='iregex', label='Тег')
    #
    #
    # name = django_filters.CharFilter()
    # rating__gt = django_filters.NumberFilter(field_name='rating', lookup_expr='gt')
    # rating__lt = django_filters.NumberFilter(field_name='rating', lookup_expr='lt')
    #
    # class Meta:
    #     model = Company
    #     fields = ['name', 'rating']

    # class Meta:
    #     model = Company
    #     fields = {
    #                 'name': ['iregex'],
    #                 'rating': ['gte'],
    #                 'time_create': ['iregex'],
    #               }