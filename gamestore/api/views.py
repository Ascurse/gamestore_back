from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .filters import GamesFilter
from .models import Game, Genre, News
from .serializers import (GameCreateSerializer, GameSerializer,
                          GenreSerializer, NewsSerializer)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', ]
    lookup_field = 'slug'


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = GamesFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return GameSerializer
        return GameCreateSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', ]
