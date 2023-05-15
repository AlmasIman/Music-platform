# Generated by Django 4.1.7 on 2023-05-15 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0014_remove_user_favorites'),
        ('music', '0012_alter_song_options_remove_song_favourite_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'verbose_name': 'Song', 'verbose_name_plural': 'Song'},
        ),
        migrations.RemoveField(
            model_name='song',
            name='favorites',
        ),
        migrations.RemoveField(
            model_name='song',
            name='id',
        ),
        migrations.AddField(
            model_name='song',
            name='song_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='year',
            field=models.CharField(choices=[('2023', '2023'), ('2022', '2022'), ('2021', '2021'), ('2020', '2020'), ('2019', '2019'), ('2018', '2018'), ('2017', '2017'), ('2016', '2016'), ('2015', '2015'), ('2014', '2014'), ('2013', '2013'), ('2012', '2012'), ('2011', '2011'), ('2010', '2010'), ('2009', '2009'), ('2008', '2008'), ('2007', '2007'), ('2006', '2006'), ('2005', '2005'), ('2004', '2004'), ('2003', '2003'), ('2002', '2002'), ('2001', '2001'), ('2000', '2000'), ('1995', '1995'), ('1990', '1990'), ('1985', '1985')], default='2023', max_length=20),
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]
