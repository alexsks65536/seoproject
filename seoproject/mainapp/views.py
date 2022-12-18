import os

from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.template import Template, Context
from .forms import FeedBackForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import *
from .models import *
from .utils import DataMixin
from dotenv import load_dotenv

load_dotenv()

menu = [{'title': 'Главная', 'url_name': 'index'},
        {'title': 'Оставить отзыв', 'url_name': 'add_review'},
        {'title': 'Связаться с нами', 'url_name': 'contact'}
        ]
sitevars = SiteVars.objects.all()
services = Services.objects.all()


class Index(ListView, DataMixin):
    paginate_by = 10
    model = Company
    template_name = 'mainapp/index.html'  # указываем путь к шаблону
    context_object_name = 'company'  # переменная контекста

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        company_all = Company.objects.all()
        count_company = len(company_all)  # кол-во клиник
        context['count_company'] = count_company
        context['menu'] = menu
        c_def = self.get_user_context(title=context['company'])

        return dict(list(context.items()) + list(c_def.items()))  # объединение словарей для передачи контекста

    def __mul__(self, other):
        return Index(self.value * other.value)

    def get_queryset(self, *, object_list=None, **kwargs):
        """
        Выбор отзывов, которые помечены для публикации
        """
        return Company.objects.filter(is_published=True)


class ShowCompany(DetailView, DataMixin):
    model = Company
    template_name = 'mainapp/show_company.html'  # указываем путь к шаблону
    context_object_name = 'company'  # переменная контекста
    slug_url_kwarg = 'company_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        company_all = Company.objects.all()
        count_company = len(company_all)  # кол-во клиник
        context['count_company'] = count_company
        context['menu'] = menu
        c_def = self.get_user_context(title=context['company'])

        return dict(list(context.items()) + list(c_def.items()))  # объединение словарей для передачи контекста


class AddReview(CreateView, ListView, DataMixin):  # Добавить отзыв

    class Meta:
        model = Reviews
        fields = ['name', 'from_email', 'company', 'message', 'stars']

    def get(self, request, *args, **kwargs):
        form = AddReviewForm()
        return render(request, 'mainapp/add_review.html', context={
            'form': form,
            'title': 'Отзыв о клинике',
            'menu': menu,
            'sitevars': sitevars,
            'services': services,
        })

    def post(self, request, *args, **kwargs):
        form = AddReviewForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            company = form.cleaned_data['Company']
            description = form.cleaned_data['description']
            stars = form.cleaned_data['stars']

            Reviews.objects.create(name=name, email=email, Company=company, description=description, stars=stars)

            try:
                send_mail(f'От {name} | {email} | {company}', description, email, [os.getenv('EMAIL_HOST_USER')])
            except BadHeaderError:
                return HttpResponse('Невалидный заголовок')
            return HttpResponseRedirect('success')
        return render(request, 'mainapp/add_review.html', context={
            'form': form,
        })


class FeedBackView(View):

    def get(self, request, *args, **kwargs):
        form = FeedBackForm()
        return render(request, 'mainapp/contact.html', context={
            'form': form,
            'title': 'Написать мне',
            'menu': menu,
            'sitevars': sitevars,
            'services': services,
        })

    def post(self, request, *args, **kwargs):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(f'От {name} | {from_email} | {subject}', message, from_email, [os.getenv('EMAIL_HOST_USER')])
            except BadHeaderError:
                return HttpResponse('Невалидный заголовок')
            return HttpResponseRedirect('success')
        return render(request, 'mainapp/contact.html', context={
            'form': form,
        })


class SuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mainapp/success.html', context={
            'title': 'Спасибо',
            'menu': menu,
            'sitevars': sitevars,
            'services': services,
        })


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
