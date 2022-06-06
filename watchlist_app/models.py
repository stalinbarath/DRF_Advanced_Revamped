from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from sqlalchemy import ForeignKey

# Create your models here.
class Platform(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField()

    def __str__(self):
        return self.name

class Watchlist(models.Model):
    title = models.CharField(max_length=255)
    storyline = models.CharField(max_length=255)
    cast = models.CharField(max_length=255)
    available_on = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='watchlist')
    registered_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=255)
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE, related_name  ='reviews')
    added_on = models.DateField(auto_now=True)

    def __str__(self):
        return f'{int(self.rating)} - {self.watchlist.title}'