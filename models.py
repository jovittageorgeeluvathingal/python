from django.db import models

class product(models.Model):
    name =  models.CharField(max_length=255)
    price =models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2550)

