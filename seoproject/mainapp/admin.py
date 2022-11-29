from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Reviews, Company

admin.site.register(Reviews)
admin.site.register(Company)