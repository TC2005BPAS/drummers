from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TopScore(models.Model):
    userId = models.IntegerField()
    minutosJugados = models.IntegerField()

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
