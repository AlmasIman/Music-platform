# Generated by Django 4.1.6 on 2023-05-13 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_change_image_field'),
    ]

    operations = [
        migrations.DeleteModel(
            name='News',
        ),
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(blank=True, help_text='The image of the song', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='song',
            name='song',
            field=models.FileField(null=True, upload_to='songs'),
        ),
    ]
