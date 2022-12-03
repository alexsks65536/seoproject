from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', include('mainapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
