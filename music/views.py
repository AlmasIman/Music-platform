from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.db.models import Q
from .models import Song, Singer
from .models import Genre
import random
from .forms import SongForm

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
        form = SignUpForm(request.POST)
        if password1!=password2:
            messages.info(request, "The passwords are different!")
        elif User.objects.filter(username=username).exists():
            messages.info(request, "This username is already taken")
        elif str(password1).__contains__("[+]"):
            messages.info(request, "The password should contain [+*.|()${}]")
        elif len(str(password1))<8:
            messages.info(request, "The password length shouldn't be less than 8")
        else:
            messages.success(request, "Successfully signed up")
            form.save()
            return redirect("login")
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
            # if request.user.is_superuser:
            #     return redirect('http://127.0.0.1:8000/admin/')
            # else:
                login(request, user)
                return redirect('main')

        else:
            messages.info(request, "Username or password is incorrect!")
    return render(request, 'registration/login.html')

def Logout(request):
    logout(request)
    return render(request, 'admin/logout.html')

