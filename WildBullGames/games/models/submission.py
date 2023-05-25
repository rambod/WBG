# games/models/submission.py

from django.db import models
from django.contrib.auth.models import User


class Submission(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    developer = models.ForeignKey(User, on_delete=models.CASCADE)
    submission_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=255, default='pending')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Submission for {self.game.title} by {self.developer.username}"
