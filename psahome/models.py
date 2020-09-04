from django.db import models

# Create your models here.

class Homelem(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
