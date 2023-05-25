# games/serializers/game_serializer.py

from rest_framework import serializers
from ..models import Game, Review, Platform


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'user', 'rating', 'comment', 'created_at')


class GameSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'developer', 'release_date', 'reviews')

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'