from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from .models import Song, Singer
import random

""" 
def favourite_add(request, id):
    post = get_object_or_404(Song, id=id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
        
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def favourite_list(request):
    new = Song.newmanager.filter(favourites=request.user)
    return render(request, '../templates/favourite.html', {'new':new})
 """

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
    return render(request, "homePage.html", context)

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

def search(request):
    if 'query' in request.GET:
        query = request.GET['query']
        multiple_q = Q(Q(name__icontains=query) | Q(year__icontains=query) | Q(singer__name__icontains = query) | Q(singer__group_name__icontains = query) |Q(genre__name__icontains = query))
        song = Song.objects.filter(multiple_q)
    else:
        song = Song.objects.all()
    context = {
        'song': song
    }
    return render(request, 'music/search.html', context)

def show_artist(request, singer_id):
    singer = get_object_or_404(Singer, pk=singer_id)

    songs = Song.objects.filter(singer=singer)

    context = {
        'singer': singer,
        'songs': songs,
        
    }

    return render(request, 'artistPage.html', context)
