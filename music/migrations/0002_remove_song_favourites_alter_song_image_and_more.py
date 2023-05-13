# Generated by Django 4.1.6 on 2023-05-13 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='favourites',
        ),
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(blank=True, help_text='The image of the song', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(help_text='The name of the song', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='song',
            field=models.FileField(blank=True, null=True, upload_to='songs'),
        ),
        
        migrations.AlterField(
        model_name='song',
        name='image',
        field=models.ImageField(upload_to='images/', default='default_image.jpg'),
        ),
]

