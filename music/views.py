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

def show_playlist(request):
    songs = Song.objects.all()
    singer = Singer.objects.all()
    music_list = list(Song.objects.all().values())
    context = {
        'songs': songs,
        'singer': singer,
        'music_list':music_list
    }
    return render(request, "playlist.html", context)