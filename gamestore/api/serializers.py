from rest_framework import serializers

from .models import Game, Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug', 'color')


class GameSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True, many=True)

    class Meta:
        model = Game
        fields = ('__all__')


class GameCreateSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(), slug_field='slug', many=True
    )

    class Meta:
        fields = ('__all__')
        model = Game
