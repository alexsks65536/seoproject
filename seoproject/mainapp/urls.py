from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('add_review/', AddReview.as_view(), name='add_review'),
    path('contact/', Contact.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('show_company/<slug:company_slug>/', ShowCompany.as_view(), name='show_company'),
    ]
