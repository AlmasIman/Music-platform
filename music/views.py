from django.shortcuts import get_object_or_404, render,redirect
from django.db.models import Q
from .models import Song, Singer, Genre
from .forms import SongForm, SignUpForm
import random
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import re

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

@login_required
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

def show_playlist(request):
    songs = Song.objects.all()
    singer = Singer.objects.all()
    context = {
        'songs': songs,
        'singer': singer
    }
    return render(request, "playlistPage.html", context)

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


def change(request, pk):
    error = ''
    song = Song.objects.get(pk=pk)
    if request.method == 'POST':
        delete = None
        if 'deler' in request.POST.keys():
            song.delete()
            return redirect('main')
        else:
            song.name = request.POST.get('name')
            singer_name = request.POST.get('singer')
            song.singer = Singer.objects.get(name=singer_name)
            genre_name = request.POST.get('genre')
            song.genre = Genre.objects.get(name=genre_name)
            song.year = request.POST.get('year')
            song.save()
            return redirect('main')
    data = {
        'error': error,
        'song': song,
    }

    return render(request, 'music/change.html', data)


def add(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save()
            return redirect('main')
    else:
        form = SongForm()
    return render(request, 'music/add.html', {'form': form})

def show_artist(request, singer_id):
    singer = get_object_or_404(Singer, pk=singer_id)

    songs = Song.objects.filter(singer=singer)

    context = {
        'singer': singer,
        'songs': songs,
        
    }
    return render(request, 'artistPage.html', context)

def SignupPage(request):
    form = SignUpForm()
    if request.method=='POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        username = request.POST.get('username')
        email = request.POST.get('email')
        form = SignUpForm(request.POST)
        if password1!=password2:
            messages.info(request, "The passwords are different!")
            redirect('signup')
        if User.objects.filter(username=username).exists():
            messages.info(request, "This username is already taken")
            redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.info(request, "This email is already used")
            redirect('signup')
        if len(str(password1))<8:
            messages.info(request, "The password length shouldn't be less than 8")
            redirect('signup')
        if not (re.findall("[+]", str(password1)) or re.findall("!", str(password1))):
            messages.info(request, "The password should contain at least one of these [+*.|()${}!]")
            redirect('signup')
        else:
            messages.success(request, "Successfully signed up")
            form.save()
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'registration/signup.html', context)

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.info(request, "Username or password is incorrect!")
    return render(request, 'registration/login.html')

def Logout(request):
    logout(request)
    return render(request, 'admin/logout.html')

@login_required
def favourites(request):
    favourite_songs = request.user.favourites.all()
    context = {
        'favourite_songs': favourite_songs
    }
    return render(request, 'favourites.html', context)

@login_required
def like_song(request, song_id):
    if request.method == 'POST':
        try:
            song = Song.objects.get(id=song_id)
            song.favourites.add(request.user)
            return redirect('favourites')
        except Song.DoesNotExist:
            pass
    return redirect('main')

@login_required
def unlike_song(request, song_id):
    if request.method == 'POST':
        try:
            song = Song.objects.get(id=song_id)
            song.favourites.remove(request.user)
            return redirect('favourites')
        except Song.DoesNotExist:
            pass
    return redirect('main')



# def create_playlist(request):
#     if request.method == 'POST':
#         form = PlaylistForm(request.POST)
#         if form.is_valid():
#             playlist = form.save(commit=False)
#             playlist.user = request.user
#             playlist.save()
#             return redirect('playlist')
#     else:
#         form = PlaylistForm()
    
#     return render(request, 'create_playlist.html', {'form': form})

# @login_required
# def add_song_to_playlist(request, playlist_id, song_id):
#     if request.method == 'POST':
#         try:
#             playlist = Playlist.objects.get(id=playlist_id, user=request.user)
#             song = Song.objects.get(id=song_id)
#             playlist.songs.add(song)
#             return redirect('home_page')
#         except (Playlist.DoesNotExist, Song.DoesNotExist):
#             return redirect('home_page')
#     else:
#         return redirect('home_page')
