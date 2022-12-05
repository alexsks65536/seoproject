from .models import *


message = 'Нажмите на заголовок, чтобы отсортировать колонку!'


class DataMixin:  # подключение модели Reviews
    def get_user_context(self, **kwargs):
        context = kwargs
        reviews = Reviews.objects.all()
        context['reviews'] = reviews
        context['message'] = message

        return context