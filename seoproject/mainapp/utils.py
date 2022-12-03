from .models import *


class DataMixin:  # подключение модели Reviews
    def get_user_context(self, **kwargs):
        context = kwargs
        reviews = Reviews.objects.all()
        context['reviews'] = reviews

        return context