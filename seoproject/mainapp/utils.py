"""
Класс содержит дополнительные переменные и таблицы БД,
которые подключаются к контексту в классах view
"""
from django.template import Template, Context
from .models import *


message = 'Нажмите на заголовок, чтобы отсортировать колонку!'


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        reviews = Reviews.objects.filter(is_published=True).all()  # таблица отзывы
        services = Services.objects.all()  # таблица услуги
        count_reviews = len(reviews)  # кол-во отзывов в общем
        context['count_reviews'] = count_reviews
        context['reviews'] = reviews
        context['services'] = services
        context['message'] = message
        template = """<i class="fa fa-star" ></i>"""  # шаблон для рисования звезд рейтинга
        t = Template(template)
        c = Context({})
        context['t'] = t.render(c)
        context['count_four'] = list(range(1, 5))  # счетчик для вывода объектов в цикле

        return context

