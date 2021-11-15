from django.db import models


class pay_order(models.Model):
    order_id = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
