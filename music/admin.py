from django.contrib import admin

from .models import Singer, Genre, Song, User,News

# Register your models here.

class singerAdmin(admin.ModelAdmin): 
    list_display = ('name', 'group_name')

class song(admin.ModelAdmin):
    list_display = ('name', 'singer', 'genre', 'year')

class new(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'news')
    

admin.site.register(Singer, singerAdmin)
admin.site.register(Genre)
admin.site.register(Song, song)
admin.site.register(User)
admin.site.register(News)

