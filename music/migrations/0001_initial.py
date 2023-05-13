# Generated by Django 4.1.6 on 2023-05-12 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The genre', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(blank=True, help_text='The image of the song', upload_to='images')),
                ('news', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Singer', help_text='Name of the singer', max_length=100)),
                ('group_name', models.CharField(help_text='The name of the group', max_length=50)),
                ('image', models.ImageField(blank=True, help_text='The image of the singer', upload_to='singer')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(help_text='The nickname of the user', max_length=50)),
                ('email', models.EmailField(help_text='The email of the user', max_length=100)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='The name of the song', max_length=200)),
                ('year', models.CharField(choices=[('2023', '2023'), ('2022', '2022'), ('2021', '2021'), ('2020', '2020'), ('2019', '2019'), ('2018', '2018'), ('2017', '2017'), ('2016', '2016'), ('2015', '2015'), ('2014', '2014'), ('2013', '2013'), ('2012', '2012'), ('2011', '2011'), ('2010', '2010'), ('2009', '2009'), ('2008', '2008'), ('2007', '2007'), ('2006', '2006'), ('2005', '2005'), ('2004', '2004'), ('2003', '2003'), ('2002', '2002'), ('2001', '2001'), ('2000', '2000'), ('1995', '1995'), ('1990', '1990'), ('1985', '1985')], default='2023', max_length=20)),
                ('image', models.ImageField(blank=True, help_text='The image of the song', upload_to='images')),
                ('song', models.FileField(null=True, upload_to='songs')),
                ('favourites', models.ManyToManyField(blank=True, related_name='favourite', to=settings.AUTH_USER_MODEL)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.genre')),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.singer')),
            ],
            options={
                'verbose_name': 'Song',
                'verbose_name_plural': 'Song',
            },
        ),
    ]
