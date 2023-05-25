# games/models/game.py

from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    developer = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='game_covers/')
    genre = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    platforms = models.ManyToManyField('Platform')

    def __str__(self):
        return self.title


class Platform(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
