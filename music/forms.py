from django import forms 
from .models import Song
from django.forms import ModelForm, TextInput
from .models import Song, Singer

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'singer', 'genre', 'year', 'image', 'song']