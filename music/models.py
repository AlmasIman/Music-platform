from django.db import models

# Create your models here.
class Singer(models.Model):
    fist_name = models.CharField \
        (max_length= 50, \
         help_text= "Fist name of the author")
    last_name = models.CharField \
        (max_length=50, \
         help_text="Last name of the author")
    # image = models.ImageField(upload_to="images",\
    #                           help_text="The image of the singer")

class Song(models.Model):
    name = models.CharField \
        (max_length= 50,\
         help_text="The name of the song")
    singer = models.ForeignKey \
        (Singer, on_delete=models.CASCADE)
    genre = models.CharField \
        (max_length= 50, \
         help_text= "The genre of the song")
    # image = models.ImageField(upload_to="images", \
    #                           help_text="The image of the song")

class Genre(models.Model):
    name = models.CharField \
        (max_length= 50,\
         help_text= "The genre")

class User(models.Model):
    nickname = models.CharField \
        (max_length= 50,\
         help_text= "The nickname of the user")
    email = models.EmailField \
        (max_length= 100, \
         help_text= "The email of the user")
    password = models.CharField(max_length= 30)



