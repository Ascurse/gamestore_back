# Generated by Django 3.2.13 on 2022-05-29 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_genre_color'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ('slug',), 'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AddField(
            model_name='game',
            name='video',
            field=models.CharField(blank=True, max_length=500, verbose_name='Game Video'),
        ),
    ]
