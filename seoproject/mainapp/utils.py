"""
Класс содержит дополнительные переменные и таблицы БД,
которые подключаются к контексту в классах view
"""

from .models import *


message = 'Нажмите на заголовок, чтобы отсортировать колонку!'


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        reviews = Reviews.objects.all()  # таблица отзывы
        services = Services.objects.all()  # таблица услуги
        count_reviews = len(reviews)  # кол-во отзывов в общем
        context['count_reviews'] = count_reviews
        context['reviews'] = reviews
        context['services'] = services
        context['message'] = message

        return context