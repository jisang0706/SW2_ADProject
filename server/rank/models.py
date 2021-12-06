from django.db import models

# Create your models here.
class Ranking(models.Model):
    userName = models.TextField(default="", blank=True)
    score = models.IntegerField(default=0, blank=True)