from django.shortcuts import render

from .models import Song, Singer

# Create your views here.
def main(request):
    songs = Song.objects.all()
    singer = Singer.objects.all()
    context = {
        'songs': songs,
        'singer': singer
    }
    return render(request, "base.html", context)