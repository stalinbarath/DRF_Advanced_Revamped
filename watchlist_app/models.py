from django.db import models
from matplotlib.style import available

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
    registered_date = models.DateField()

    def __str__(self):
        return self.title