from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.template import Template, Context

from .forms import *
from .models import *
from .utils import DataMixin

menu = [{'title': 'Главная', 'url_name': 'index'},
        {'title': 'Оставить отзыв', 'url_name': 'add_review'},
        ]


class Index(ListView, DataMixin):
    paginate_by = 10
    model = Company
    template_name = 'mainapp/index.html'  # указываем путь к шаблону
    context_object_name = 'company'  # переменная контекста

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        template = """<i class="fa fa-star" ></i>"""
        t = Template(template)
        c = Context({})
        context['t'] = t.render(c)
        c_def = self.get_user_context(title=context['company'])

        return dict(list(context.items()) + list(c_def.items()))  # объединение словарей для передачи контекста


class AddReview(CreateView):  # Добавить отзыв
    form_class = ContactForm  # Указываем форму
    template_name = 'mainapp/add_review.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить отзыв'
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

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('index')


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
