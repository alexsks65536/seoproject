from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import *
from .models import *

menu = [{'title': 'Главная', 'url_name': 'index'},
        {'title': 'Оставить отзыв', 'url_name': 'review'},
        # {'title': 'Обратная связь', 'url_name': 'contact'},
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


class Review(CreateView):
    form_class = ContactForm
    template_name = 'mainapp/review.html'  # указываем путь к шаблону
    # context_object_name = 'review'  # переменная контекста

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


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'mainapp/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('login')
