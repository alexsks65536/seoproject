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
        reviews = Reviews.objects.filter(is_published=True)  # таблица отзывы
        services = Services.objects.filter(is_published=True)  # таблица услуги
        sitevars = SiteVars.objects.all()  # Переменные сайта
        topbanner = TopBanner.objects.all()  # Верхний баннер
        timetable = Timetable.objects.all()  # Распорядок работы
        companyphoto = CompanyPhoto.objects.filter(is_published=True)  # Фото клиник
        price = Price.objects.filter(is_published=True).order_by('price_min')  # Цены на услуги клиник сортировка по возрастанию цен
        count_reviews = len(reviews)  # кол-во отзывов в общем
        context['count_reviews'] = count_reviews
        context['reviews'] = reviews
        context['services'] = services
        context['sitevars'] = sitevars
        context['topbanner'] = topbanner
        context['timetable'] = timetable
        context['companyphoto'] = companyphoto
        context['price'] = price
        context['message'] = message
        template = """<i class="fa fa-star stars" ></i>"""  # шаблон для рисования звезд рейтинга
        t = Template(template)
        c = Context({})
        context['t'] = t.render(c)
        context['count_four'] = list(range(1, 5))  # счетчик для вывода объектов в цикле

        return context

