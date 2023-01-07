from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Reviews, Company, Services, SiteVars, TopBanner, Timetable, CompanyPhoto, Price


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_html_photo', 'stars', 'time_create', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'rating', 'stars', 'is_published')
    list_filter = ('name', 'rating', 'stars', 'time_create', 'tag', 'is_published')
    prepopulated_fields = {"slug": ("name",)}
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'Company', 'time_create', 'is_published')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'Company', 'stars', 'is_published')
    search_fields = ('name', 'Company', 'is_published')
    save_on_top = True


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'icon', 'is_published')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)
    save_on_top = True


class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'Service', 'price_min', 'price_max', 'Company', 'time_create', 'is_published')
    list_display_links = ('id', 'Service', 'Company')
    list_filter = ('Service', 'Company')
    search_fields = ('Service', 'Company')
    save_on_top = True


class SiteVarsAdmin(admin.ModelAdmin):
    # list_display = ('id', 'logo', 'head_slogan', 'site_title')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")


class TopBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_html_photo', 'textup', 'textdown')
    save_on_top = True

    def get_html_photo(self, object):
        if object.iconbanner:
            return mark_safe(f"<img src='{object.iconbanner.url}' width=30>")


class TimetableAdmin(admin.ModelAdmin):
    list_display = ('id', 'day_week', 'time_work')
    save_on_top = True


class CompanyPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_html_photo', 'description', 'Company', 'is_published')
    list_filter = ('Company',)
    search_fields = ('Company',)
    save_on_top = True

    def get_html_photo(self, object):
        if object.photoset:
            return mark_safe(f"<img src='{object.photoset.url}' width=30>")


admin.site.register(Company, CompanyAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(SiteVars, SiteVarsAdmin)
admin.site.register(TopBanner, TopBannerAdmin)
admin.site.register(Timetable, TimetableAdmin)
admin.site.register(CompanyPhoto, CompanyPhotoAdmin)
