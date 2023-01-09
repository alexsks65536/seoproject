"""
'exact' - полное совпадения названия, например 'НИАРМЕДИК'
'iexact' - работает также как 'exact'
'contains' - любое совпадение, но с учетом регистра букв
'icontains' - работает также как 'contains'
'regex' - Наименование клиники соответствует регулярному выражению
'iregex' - любые буквы или сочетания без учета регистра
"""
import django_filters


class CompanyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iregex', label='Клиника')
    rating = django_filters.NumberFilter(lookup_expr='gte', label='Рейтинг')
