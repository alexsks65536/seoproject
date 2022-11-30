from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('review/', Review.as_view(), name='review'),
    path('contact/', Contact.as_view(), name='contact'),
    ]