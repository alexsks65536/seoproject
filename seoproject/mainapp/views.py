from django.views.generic import ListView

from .models import Company, Reviews

menu = [{'title': 'Главная', 'url_name': 'index'},
        {'title': 'Оставить отзыв', 'url_name': 'review'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        ]

message = 'Нажмите на заголовок, чтобы отсортировать колонку!'


class Index(ListView):
    paginate_by = 10
    model = Company
    template_name = 'mainapp/index.html'  # указываем путь к шаблону
    context_object_name = 'company'  # переменная контекста

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['message'] = message
        star = Company.stars
        context['stars'] = [i for i in range(1, 6)]

        return context


class Review(ListView):
    model = Reviews
    template_name = 'mainapp/review.html'  # указываем путь к шаблону
    context_object_name = 'reviews'  # переменная контекста

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context


class Contact(ListView):
    model = Company
    template_name = 'mainapp/contact.html'  # указываем путь к шаблону
    context_object_name = 'company'  # переменная контекста

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context