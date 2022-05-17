from django_filters import rest_framework as filters

from .models import Game


class GamesFilter(filters.FilterSet):
    name = filters.CharFilter(
        field_name='name',
        lookup_expr='icontains'
    )
    genre = filters.CharFilter(
        field_name='genre__slug',
        lookup_expr='icontains'
    )

    class Meta:
        model = Game
        fields = ['name', 'genre', 'year']
