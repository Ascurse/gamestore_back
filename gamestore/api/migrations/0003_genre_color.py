# Generated by Django 3.2.13 on 2022-05-20 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_game_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='color',
            field=models.CharField(default='#red', max_length=20, verbose_name='Цвет категории'),
        ),
    ]