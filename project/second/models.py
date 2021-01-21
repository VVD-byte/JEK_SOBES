from django.db import models

class Accrual(models.Model):
    date = models.DateTimeField(auto_created=True)
    month = models.IntegerField()

class Payment(models.Model):
    date = models.DateTimeField(auto_created=True)
    month = models.IntegerField()