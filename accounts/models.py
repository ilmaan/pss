from django.db import models

# Create your models here.

class Account(models.Model):
    first_name = models.CharField(max_length=100)
    username = models.CharField(max_length=15)
    email = models.CharField(max_length=15)
    phonenum = models.CharField(max_length=10)
    password = models.CharField(max_length=25)
    