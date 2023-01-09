from django.contrib import admin
from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('add_review/', AddReview.as_view(), name='add_review'),
    path('add_review/success/', SuccessView.as_view(), name='success'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('show_company/<slug:company_slug>/', ShowCompany.as_view(), name='show_company'),
    path('contact/', FeedBackView.as_view(), name='contact'),
    path('contact/success/', SuccessView.as_view(), name='success'),
    path('search_company/', SearchCompany.as_view(), name='search_company'),
]
