from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Song
from django.forms import ModelForm, TextInput
from .models import Song, Singer

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# class UploadForm(forms.Form):
#     file_upload = forms.ImageField()

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'singer', 'genre', 'year', 'image', 'song']

# class PlaylistForm(forms.ModelForm):
#     class Meta:
#         model = Playlist
#         fields = ['name']

