from django.db import models


class Brewiten(models.Model):
    brew_name = models.CharField(max_length=255)
    Price = models.FloatField()
    type_brews = models.CharField(max_length=255)
