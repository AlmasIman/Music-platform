from django.db import models
from django.contrib.auth.models import User

yearOfRelease = (
    ('2023','2023'),
    ('2022','2022'),
    ('2021','2021'),
    ('2020','2020'),
    ('2019','2019'),
    ('2018','2018'),
    ('2017','2017'),
    ('2016','2016'),
    ('2015', '2015'),
    ('2014', '2014'),
    ('2013', '2013'),
    ('2012', '2012'),
    ('2011', '2011'),
    ('2010', '2010'),
    ('2009', '2009'),
    ('2008', '2008'),
    ('2007', '2007'),
    ('2006', '2006'),
    ('2005', '2005'),
    ('2004','2004'),
    ('2003','2003'),
    ('2002','2002'),
    ('2001','2001'),
    ('2000','2000'),
    ('1995','1995'),
    ('1990','1990'),
    ('1985','1985'),
)

# Create your models here.
class Singer(models.Model):
    name = models.CharField \
        (max_length= 100, \
         help_text= "Name of the singer", default='Singer')
    group_name = models.CharField \
        (max_length = 50,\
            help_text="The name of the group")
    image = models.ImageField(upload_to="singer",\
                               help_text="The image of the singer", blank=True)
    
    
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField \
        (max_length= 50,\
         help_text= "The genre")
        
    def __str__(self):
        return self.name
    
class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField \
        (max_length=200,\
         help_text="The name of the song")
        
    singer = models.ForeignKey \
        (Singer, on_delete=models.CASCADE)
    
    genre = models.ForeignKey\
        (Genre, on_delete=models.CASCADE)
    
    """song_date = models.DateTimeField \
        (verbose_name= \
              "Date the song was released",\
          default='2023') """
          
    year = models.CharField(choices=yearOfRelease, max_length=20, default='2023')
    
    image = models.ImageField(upload_to="images", \
                               help_text="The image of the song", blank=True)
    song = models.FileField(upload_to='songs', null=True)

    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'Song'
        verbose_name_plural = 'Song'
        

class User(models.Model):
    nickname = models.CharField \
        (max_length= 50,\
         help_text= "The nickname of the user")
    email = models.EmailField \
        (max_length= 100, \
         help_text= "The email of the user")
    password = models.CharField(max_length= 30)



