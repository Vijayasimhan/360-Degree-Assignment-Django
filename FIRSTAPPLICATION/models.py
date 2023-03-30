from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=256)
    contact = models.IntegerField()
    address = models.CharField(max_length=256)