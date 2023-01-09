import os
from itertools import chain

from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.list import MultipleObjectMixin
from django_filters.views import FilterView

from .filters import CompanyFilter
from .forms import *
from .models import *
from .utils import DataMixin
from dotenv import load_dotenv

load_dotenv()

sitevars = SiteVars.objects.all()
topbanner = TopBanner.objects.all()
services = Services.objects.filter(is_published=True)
reviews = Reviews.objects.filter(is_published=True)

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

        c_def = self.get_user_context(title=context['company'])

        return dict(list(context.items()) + list(c_def.items()))  # объединение словарей для передачи контекста

    def __mul__(self, other):
        return Index(self.value * other.value)

    def get_queryset(self, *, object_list=None, **kwargs):
        """
        Выбор отзывов, которые помечены для публикации
        """
        return Company.objects.filter(is_published=True)


class ShowCompany(DetailView, MultipleObjectMixin, DataMixin):
    model = Company
    template_name = 'mainapp/show_company.html'  # указываем путь к шаблону
    paginate_by = 5
    slug_url_kwarg = 'company_slug'

    def get_context_data(self, **kwargs):
        object_list = Reviews.objects.filter(name=self.object)
        context = super(ShowCompany, self).get_context_data(object_list=object_list, **kwargs)
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
            'sitevars': sitevars,
            'services': services,
            'topbanner': topbanner,
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
            'sitevars': sitevars,
            'services': services,
            'topbanner': topbanner,
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
            'sitevars': sitevars,
            'services': services,
            'topbanner': topbanner,
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


class SearchCompany(ListView, DataMixin):
    def get(self, request, *args, **kwargs):
        company_list = Company.objects.all().order_by('name')
        company_filter = CompanyFilter(request.GET, queryset=company_list)
        return render(request, 'mainapp/company_list.html',
                      {'filter': company_filter,
                       'sitevars': sitevars,
                       'topbanner': topbanner,
                       'services': services,
                       }
                      )
