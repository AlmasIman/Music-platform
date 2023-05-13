from django.contrib import admin

from .models import Singer, Genre, Song

# Register your models here.

class singerAdmin(admin.ModelAdmin): 
    list_display = ('name', 'group_name')

class song(admin.ModelAdmin):
    list_display = ('name', 'singer', 'genre', 'year')
    

admin.site.register(Singer, singerAdmin)
admin.site.register(Genre)
admin.site.register(Song, song)

