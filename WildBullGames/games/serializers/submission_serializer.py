# games/serializers/submission_serializer.py

from rest_framework import serializers
from ..models import Submission


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ('id', 'game', 'developer', 'submission_date', 'status')
