from django.db import models


# Create your models here.
class train(models.Model):
    number = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    source = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)


class stations(models.Model):
    station = models.CharField(max_length=20)


