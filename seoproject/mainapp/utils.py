from mainapp.models import *

"""
Главное меню
"""
menu = [{'title': 'Главная', 'url_name': 'index'},
        {'title': 'Оставить отзыв', 'url_name': 'review'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
       ]
rating = [1, 2, 3, 4]

class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        prods = Product.objects.all()

        user_menu = menu.copy()  # делаем копию меню.
        # if not self.request.user.is_authenticated:  # если user не авторизован, убираем пункт меню "Добавить статью"
        #     user_menu.pop(1)

        context['menu'] = user_menu
        context['rating'] = rating
        context['prods'] = prods
        if 'prod_selected' not in context:  # Переопределить ключ prod_selected = 0, если его нет в **kwargs
            context['prod_selected'] = 0
        return context
