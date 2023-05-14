from django.urls import path
from . import views
from music.views import *
from django.conf import settings
from django.conf.urls.static import static

# from django.conf.urls import url


urlpatterns = [
   path('main/', views.main, name='main'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('add/',views.add, name='add'),
    path('change/<int:pk>/',views.change, name='change'),
    #path('fav/<int:id>/', views.favourite_add, name='favourite_add'),
    #path('favourites', views.favourite_list, name='favourite_list'),
    path('artist/<int:singer_id>/', views.show_artist, name='show_artist'),
    path('', views.LoginPage, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('signup/', views.SignupPage, name='signup'),
    path('playList/', views.show_playlist, name="show_playlist")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
