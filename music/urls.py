from django.urls import path
from . import views
from music.views import *
# from django.conf.urls import url


urlpatterns = [
    path('', views.main, name='main'),
    
]