from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('add_review/', AddReview.as_view(), name='add_review'),
    path('index/success/', Index.as_view(), name='succes'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('show_company/<slug:company_slug>/', ShowCompany.as_view(), name='show_company'),
    path('contact/', FeedBackView.as_view(), name='contact'),
    path('contact/success/', SuccessView.as_view(), name='succes'),
    ]
