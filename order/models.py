from django.db import models


# Create your models here.
class order_info(models.Model):
    order_id = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100)
    time = models.TimeField(auto_now_add=True)
    train_number = models.CharField(max_length=20)
    departure = models.CharField(max_length=20)
    arrival = models.CharField(max_length=20)
    amount = models.IntegerField(default=0)
