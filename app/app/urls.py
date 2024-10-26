from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
import app.settings as settings
import main.urls as main_urls

from django.conf import settings
from django.conf.urls.static import static

from main import views as main_views, urls as main_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include(main_urls.api_urlpatterns)),
    path('', include(main_urls.urlpatterns)),
    path('news/', include('news.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),