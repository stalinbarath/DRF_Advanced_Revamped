from django.db import models

# Create your models here.
class Watchlist(models.Model):
    title = models.CharField(max_length=255)
    storyline = models.CharField(max_length=255)
    cast = models.CharField(max_length=255)
    registered_date = models.DateField()

    def __str__(self):
        return self.title