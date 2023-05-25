# games/serializers/screenshot_serializer.py

from rest_framework import serializers
from ..models import Screenshot


class ScreenshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screenshot
        fields = ('id', 'game', 'image', 'caption')
