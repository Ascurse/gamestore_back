from django.contrib import admin

from .models import Game, Genre, News


@admin.register(Genre)
class GenreAdminConfig(admin.ModelAdmin):
    list_display = (
        'name',
        'slug'
    )


@admin.register(Game)
class GameAdminConfig(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'year',
        'image'
    )


@admin.register(News)
class NewsAdminConfig(admin.ModelAdmin):
    list_display = (
        'title',
        'post',
        'created_at',
        'post_image',
        'related_game'
    )
