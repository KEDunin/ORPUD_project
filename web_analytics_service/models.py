from django.db import models
class Shop(models.Model):
    name = models.CharField(max_length=50)


class Iphone(models.Model):
    number = models.IntegerField()
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    memory = models.CharField(max_length=30)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    price = models.IntegerField(null=True)

