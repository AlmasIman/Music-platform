from django.shortcuts import render,get_object_or_404

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

def detail(request,id):
    song = Song.objects.filter(song_id=id).first()
    context = {
        'song': song,
    }
    return render(request, "music/detail_songs.html", context)