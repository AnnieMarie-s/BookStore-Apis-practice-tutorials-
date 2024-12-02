from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class bookmodel(models.Model):
    title = models.CharField(max_length=100)
    langauge = models.CharField(max_length=100)
    edition = models.CharField(max_length=100)
    genere = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
