# games/models/screenshot.py

from django.db import models


class Screenshot(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='screenshots')
    image = models.ImageField(upload_to='game_screenshots/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Screenshot for {self.game.title}"
