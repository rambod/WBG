# games/models/review.py

from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.game.title} by {self.user.username}"
