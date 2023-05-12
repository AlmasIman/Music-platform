from django.shortcuts import render

from .models import Song, Singer
import random

def get_random_songs():
    songs = Song.objects.all()
    return random.sample(list(songs), 7)

# in your view function
# Create your views here.
def main(request):
    songs = Song.objects.all()
    singer = Singer.objects.all()
    random_songs = get_random_songs()
    context = {
        'songs': songs,
        'singer': singer,
        'random_songs':random_songs
    }
    return render(request, "base.html", context)

""" def show_playlist(request):
    songs = Song.objects.all()
    singer = Singer.objects.all()
    music_list = list(Song.objects.all().values())
    context = {
        'songs': songs,
        'singer': singer,
        'music_list':music_list
    }
    return render(request, "playlist.html", context) """

def detail(request,id):
    song = Song.objects.filter(song_id=id).first()
    context = {
        'song': song,
    }
    return render(request, "music/detail_songs.html", context)

