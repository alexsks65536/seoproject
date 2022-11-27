from django.shortcuts import render
from django.views.generic import ListView

from .models import Company
from .utils import *


class Index(ListView, DataMixin):
    model = Company
    template_name = "mainapp/index.html"  # указываем путь к шаблону
    context_object_name = "posts"  # переменная контекста

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     """
    #     Передача динамического контекста
    #     """
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title="Главная страница")
    #     return dict(list(context.items()) + list(c_def.items()))  # объединение словарей для передачи контекста

    # def get_queryset(self):
    #     """
    #     Выбор постов, которые помечены для публикации
    #     """
    #     return Company.objects.filter(is_published=True).select_related('prod')
    #     # select_related - отложенный запрос для уменьшения нагрузки на БД


class About(ListView, DataMixin):
    model = Company
    template_name = "mainapp/about.html"  # указываем путь к шаблону
    context_object_name = "posts"  # переменная контекста

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Передача динамического контекста
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="О компании")
        return dict(list(context.items()) + list(c_def.items()))  # объединение словарей для передачи контекста

    def get_queryset(self):
        """
        Выбор постов, которые помечены для публикации
        """
        # return Company.objects.filter(is_published=True).select_related('prod')
        # # select_related - отложенный запрос для уменьшения нагрузки на БД


class Service(ListView, DataMixin):
    model = Company
    template_name = "mainapp/service.html"  # указываем путь к шаблону
    context_object_name = "posts"  # переменная контекста

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Передача динамического контекста
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Сервис")
        return dict(list(context.items()) + list(c_def.items()))  # объединение словарей для передачи контекста

    def get_queryset(self):
        """
        Выбор постов, которые помечены для публикации
        """
        # return Company.objects.filter(is_published=True).select_related('prod')
        # # select_related - отложенный запрос для уменьшения нагрузки на БД


class Review(ListView, DataMixin):
    model = Company
    template_name = "mainapp/review.html"  # указываем путь к шаблону
    context_object_name = "posts"  # переменная контекста

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Передача динамического контекста
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Блог")
        return dict(list(context.items()) + list(c_def.items()))  # объединение словарей для передачи контекста

    def get_queryset(self):
        """
        Выбор постов, которые помечены для публикации
        """
        # return Company.objects.filter(is_published=True).select_related('prod')
        # # select_related - отложенный запрос для уменьшения нагрузки на БД


class Contact(ListView, DataMixin):
    model = Company
    template_name = "mainapp/contact.html"  # указываем путь к шаблону
    context_object_name = "posts"  # переменная контекста

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Передача динамического контекста
        """
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Блог")
        return dict(list(context.items()) + list(c_def.items()))  # объединение словарей для передачи контекста

    def get_queryset(self):
        """
        Выбор постов, которые помечены для публикации
        """
        # return Company.objects.filter(is_published=True).select_related('prod')
        # # select_related - отложенный запрос для уменьшения нагрузки на БД
