from django.urls import path, re_path
from mainapp.views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('service/', Service.as_view(), name='service'),
    path('review/', Review.as_view(), name='review'),
    path('contact/', Contact.as_view(), name='contact'),
    ]
