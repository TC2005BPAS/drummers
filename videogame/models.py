from django.db import models

# Create your models here.

class TopScore(models.Model):
    userId = models.IntegerField()
    minutosJugados = models.IntegerField()
