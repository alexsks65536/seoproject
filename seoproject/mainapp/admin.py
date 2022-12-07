from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Reviews, Company, Services


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create', 'get_html_photo', 'stars')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'rating', 'stars')
    list_filter = ('name', 'rating', 'stars', 'time_create', 'tag')
    prepopulated_fields = {"slug": ("name",)}
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'Company', 'description')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'Company', 'stars')
    search_fields = ('name', 'Company')
    save_on_top = True


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'icon')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)
    save_on_top = True


admin.site.register(Company, CompanyAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Services, ServicesAdmin)
