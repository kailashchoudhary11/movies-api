from django.db import models
from jsonfield import JSONField
# Create your models here.

class Movie(models.Model):
    id = models.CharField(max_length=250, primary_key=True)
    title = models.CharField(max_length=500)
    rating = models.CharField(max_length=10)
    released_year = models.CharField(max_length=5)
    genres = JSONField()
