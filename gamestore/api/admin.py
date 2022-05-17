from django.contrib import admin
from .models import Genre, Game

# Register your models here.
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