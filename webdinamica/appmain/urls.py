from django.urls import path, re_path
from .views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('inicio/', inicio, name='inicio')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
