from django.urls import path
from . import views
from music.views import *
from django.conf import settings
from django.conf.urls.static import static

# from django.conf.urls import url


urlpatterns = [
    path('', views.main, name='main'),
    path('show_playlist/', views.show_playlist, name='show_playlist')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)