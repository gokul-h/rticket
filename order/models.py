from django.db import models


# Create your models here.
class order(models.Model):
    transaction_id: models.CharField(max_length=100)
    customer_id: models.CharField(max_length=100)
    time: models.TimeField(auto_now_add=True)
    payment_id: models.CharField(max_length=100)
    train_number: models.CharField(max_length=20)
