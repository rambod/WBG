# games/serializers/review_serializer.py

from rest_framework import serializers
from ..models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'game', 'user', 'rating', 'comment', 'created_at')
