from django.urls import path
from . import views
from music.views import *
from django.conf import settings
from django.conf.urls.static import static

# from django.conf.urls import url


urlpatterns = [
    path('', views.main, name='main'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('add/',views.add, name='add'),
    path('change/<int:pk>/',views.change, name='change')
    #path('fav/<int:id>/', views.favourite_add, name='favourite_add'),
    #path('favourites', views.favourite_list, name='favourite_list'),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)