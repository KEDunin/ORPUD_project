from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=50)


class Iphone(models.Model):
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    memory = models.IntegerField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    price = models.IntegerField()
    date = models.DateTimeField()
    link = models.CharField(max_length=1000)
