from django.urls import path
from . import views
from music.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# from django.conf.urls import url


urlpatterns = [
    path('main/', views.main, name='main'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('add/',views.add, name='add'),
    path('change/<int:pk>/',views.change, name='change'),
    path('artist/<int:singer_id>/', views.show_artist, name='show_artist'),
    path('', views.LoginPage, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('signup/', views.SignupPage, name='signup'),
    path('playList/', views.show_playlist, name="show_playlist"),
    path('favourites/', views.favourites, name='favorites'),
    path('like_song/<int:song_id>/', views.like_song, name='like_song'),
    path('unlike_song/<int:song_id>/', views.unlike_song, name='unlike_song'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"),
         name="password_reset_complete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
