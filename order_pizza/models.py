from django.db import models


# Create your models here.
class Size(models.Model):
    inches = models.IntegerField()
    label = models.CharField(max_length=10, null=True, blank=True)
    price = models.IntegerField()
    createdOn = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    deletedOn = models.DateTimeField(null=True, blank=True)


class Topping(models.Model):
    topType = models.CharField(max_length=20)
    price = models.IntegerField()
    createdOn = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    deletedOn = models.DateTimeField(null=True, blank=True)


class PizzaOrder(models.Model):
    orderid = models.UUIDField()
    shape = models.CharField(max_length=10)
    size = models.IntegerField()
    top_type = models.CharField(max_length=20)
    amt = models.IntegerField()
    createdOn = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    deletedOn = models.DateTimeField(null=True, blank=True)
