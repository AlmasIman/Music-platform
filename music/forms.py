from django import forms 
from .models import Song
from django.forms import ModelForm, TextInput
from .models import Song, Singer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'singer', 'genre', 'year', 'image', 'song']
        
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

