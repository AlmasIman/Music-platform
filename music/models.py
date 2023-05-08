from django.db import models

# Create your models here.
class Singer(models.Model):
    fist_name = models.CharField \
        (max_length= 50, \
         help_text= "Fist name of the singer")
    last_name = models.CharField \
        (max_length=50, \
         help_text="Last name of the singer")
    group_name = models.CharField \
        (max_length = 50,\
            help_text="The name of the group")
    # image = models.ImageField(upload_to="images",\
    #                           help_text="The image of the singer")

class Genre(models.Model):
    name = models.CharField \
        (max_length= 50,\
         help_text= "The genre")
    
class Song(models.Model):
    name = models.CharField \
        (max_length= 50,\
         help_text="The name of the song")
    singer = models.ForeignKey \
        (Singer, on_delete=models.CASCADE)
    genre = models.ForeignKey\
        (Genre, on_delete=models.CASCADE)
    # song_date = models.DateField \
    #     (verbose_name= \
    #          "Date the song was released",\
    #      default=2023)
    # image = models.ImageField(upload_to="images", \
    #                           help_text="The image of the song")

class User(models.Model):
    nickname = models.CharField \
        (max_length= 50,\
         help_text= "The nickname of the user")
    email = models.EmailField \
        (max_length= 100, \
         help_text= "The email of the user")
    password = models.CharField(max_length= 30)



